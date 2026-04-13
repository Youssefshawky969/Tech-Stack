## Workflow Syntax:

### `name`

 This is the name of the workflow. GitHub displays the names of your workflows under your repository's "Actions" tab. If you omit name, GitHub displays the workflow             file path relative to the root of the repository.

  

### `on`

   To automatically trigger a workflow, use on to define which events can cause the workflow to run.
    For example you have 2 types of events.
  
   1- Single event
  
   ```yaml
    on: push
   ```
  
   2- Multiple event
  
   ```yaml
    on: [push, fork]
  ```

### `jobs`

  A workflow run is made up of one or more jobs, which run in parallel by default.

  To run jobs sequentially, you can define dependencies on other jobs using the `jobs.<job_id>.needs` keyword.

  Each job runs in a runner environment specified by `runs-on`.

  #### `jobs.<job_id>`
  
  Use `jobs.<job_id>` to give your job a unique identifier.

  The key `job_id` is a string and its value is a map of the job's configuration data. You must replace <job_id> with a string that is unique to the jobs object.

  The <job_id> must start with a letter or `_` and contain only alphanumeric characters, `-`, or `_`.

  Example: Creating jobs:

  In this example, two jobs have been created, and their `job_id` values are `my_first_job` and `my_second_job`.

  ```yaml
  jobs:
    my_first_job:
      name: My first job
    my_second_job:
      name: My second job
  ```

   #### `jobs.<job_id>.name`
   
   - Use `jobs.<job_id>.name` to set a name for the job, which is displayed in the GitHub UI.

  #### `jobs.<job_id>.needs`
    
   - Use `jobs.<job_id>.needs` to identify any jobs that must complete successfully before this job will run.
   - It can be a string or array of strings.
   - If a job fails or is skipped, all jobs that need it are skipped unless the jobs use a conditional expression that causes the job to continue. If a run contains a series of jobs that need each other, a failure or skip applies to all jobs in the dependency chain from the point of failure or skip onwards.

  If you would like a job to run even if a job it is dependent on did not succeed, use the `always()` conditional expression in `jobs.<job_id>.if`.

  Example: Requiring successful dependent jobs

  ```yaml
  jobs:
    job1:
    job2:
      needs: job1
    job3:
      needs: [job1, job2]
  ```

  The jobs in this example run sequentially:

1- job1

2- job2

3- job3

Example: Not requiring successful dependent jobs

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    if: ${{ always() }}
    needs: [job1, job2]
```

In this example, job3 uses the `always()` conditional expression so that it always runs after job1 and job2 have completed, regardless of whether they were successful.

  #### `jobs.<job_id>.runs-on`
  
  - Use `jobs.<job_id>.runs-on` to define the type of machine to run the job on.
  - The destination machine can be either a GitHub-hosted runner, larger runner, or a self-hosted runner.
  - You can target runners based on the labels assigned to them, or their group membership, or a combination of these.
  - You can provide runs-on as:

    - A single string
    - A single variable containing a string
    - An array of strings, variables containing strings, or a combination of both
    - A key: value pair using the group or labels keys

Example: Specifying an operating system

```yaml
runs-on: ubuntu-latest
```

#### `jobs.<job_id>.steps`

A job contains a sequence of tasks called `steps`

Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in a Docker registry.

Not all steps run actions, but all actions run as a step. Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps. GitHub provides built-in steps to set up and complete a job.

Example of `jobs.<job_id>.steps`:

```yaml
name: Greeting from Mona          # name of the workflow

on: push                          # type of trigger

jobs:                             # Idenfity the jobs
  my-job:                         # idenfiy the first job
    name: My Job                  # name of the first job
    runs-on: ubuntu-latest        # specify the runner type 
    steps:                        # Identfiy the steps
      - name: Print a greeting    # Step name
        env:                      # Identfiy the enviroment var
          MY_VAR: Hi there! My name is
          FIRST_NAME: Mona
          MIDDLE_NAME: The
          LAST_NAME: Octocat
        run: |                    # The action itself
          echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```
##### `jobs.<job_id>.steps[*].uses`

Selects an action to run as part of a step in your job. An action is a reusable unit of code. You can use an action defined in the same repository as the workflow, a public repository, or in a published Docker container image.

Thet strongly recommend that you include the version of the action you are using by specifying a Git ref, SHA, or Docker tag. If you don't specify a version, it could break your workflows or cause unexpected behavior when the action owner publishes an update.

Example: Using versioned actions

```yaml
steps:
  # Reference a specific commit
  - uses: actions/checkout@8f4b7f84864484a7bf31766abe9204da3cbe65b3
  # Reference the major version of a release
  - uses: actions/checkout@v5
  # Reference a specific version
  - uses: actions/checkout@v5.2.0
  # Reference a branch
  - uses: actions/checkout@main
```

Example: Using a public action

`{owner}/{repo}@{ref}`

You can specify a branch, ref, or SHA in a public GitHub repository.

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        # Uses the default branch of a public repository
        uses: actions/heroku@main
      - name: My second step
        # Uses a specific version tag of a public repository
        uses: actions/aws@v2.0.1
```

Example: Using a public action in a subdirectory

`{owner}/{repo}/{path}@{ref}`

A subdirectory in a public GitHub repository at a specific branch, ref, or SHA.

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/aws/ec2@main
```

Example: Using an action in the same repository as the workflow

`./path/to/dir`

The path to the directory that contains the action in your workflow's repository. You must check out your repository before using the action.

```text
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
```

The path is relative (`./`) to the default working directory (github.workspace, $GITHUB_WORKSPACE). If the action checks out the repository to a location different than the workflow, the relative path used for local actions must be updated.

Example workflow file:

```yaml
jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - name: My first step - check out repository
        uses: actions/checkout@v5
      # This step references the directory that contains the action.
      - name: Use local hello-world-action
        uses: ./.github/actions/hello-world-action
```

##### `jobs.<job_id>.steps[*].run`

Runs command-line programs that do not exceed 21,000 characters using the operating system's shell. If you do not provide a name, the step name will default to the text specified in the run command.

Commands run using non-login shells by default. You can choose a different shell and customize the shell used to run commands.

Each run keyword represents a new process and shell in the runner environment. When you provide multi-line commands, each line runs in the same shell. For example:

- A single-line command:

  ```yaml
  - name: Install Dependencies
  run: npm install
  ```

- A multi-line command:

```yaml
- name: Clean install dependencies and build
  run: |
    npm ci
    npm run build
```

##### `jobs.<job_id>.steps[*].working-directory`

Using the `working-directory` keyword, you can specify the working directory of where to run the command.

```yaml
- name: Clean temp directory
  run: rm -rf *
  working-directory: ./temp
```




