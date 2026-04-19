## Workflow Syntax

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

## Events that trigger workflows

You can configure your workflows to run when specific activity on GitHub happens, at a scheduled time, or when an event outside of GitHub occurs.

Workflow triggers are events that cause a workflow to run. For more information about how to use workflow triggers

### `Push`

Runs your workflow when you push a commit or tag, or when you create a repository from a template.

For example, you can run a workflow when the push event occurs.

```yaml
on:
  push
```
> [!NOTE]
> When a push webhook event triggers a workflow run, the Actions UI's "pushed by" field shows the account of the pusher and not the author or committer. However, if the changes are pushed to a repository using SSH authentication with a deploy key, then the "pushed by" field will be the repository admin who verified the deploy key when it was added it to a repository.

#### Running your workflow only when a push to specific branches occurs

You can use the `branches` or `branches-ignore` filter to configure your workflow to only run when specific branches are pushed.

For example, this workflow will run when someone pushes to `main` or to a branch that starts with `releases/`.

```yaml
on:
  push:
    branches:
      - 'main'
      - 'releases/**'
```

> [!NOTE]
> If you use both the branches filter and the paths filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a push that includes a change to a JavaScript (.js) file is made to a branch whose name starts with releases/:
> ```yaml
> on:
>   push
>     branches:
>       - 'releases/**'
>     paths
>       - '**.js'
> ```

#### Running your workflow only when a push of specific tags occurs

You can use the `tags` or `tags-ignore` filter to configure your workflow to only run when specific tags are pushed.

For example, this workflow will run when someone pushes a tag that starts with `v1`.

```yml
on:
  push:
    tags:
      - v1.**
```

#### Running your workflow only when a push affects specific files

You can use the paths or paths-ignore filter to configure your workflow to run when a push to specific files occurs.

For example, this workflow will run when someone pushes a change to a JavaScript file (`.js`):

```yaml
on:
  push:
    paths:
      - '**.js'
```

### `pull request`

Runs your workflow when activity on a pull request in the workflow's repository occurs. For example, if no activity types are specified, the workflow runs when a pull request is opened or reopened or when the head branch of the pull request is updated.

For activity related to pull request reviews, pull request review comments, or pull request comments, use the `pull_request_review`, `pull_request_review_comment`, or `issue_comment` events instead.

> [!NOTE]
> Note that `GITHUB_SHA` for this event is the last merge commit of the pull request merge branch.
> 
> If you want to get the commit ID for the last commit to the head branch of the pull request, use `github.event.pull_request.head.sha` instead.

For example, you can run a workflow when a pull request has been opened or reopened.

```yaml
on:
  pull_request:
    types: [opened, reopened]
```
You can use the event context to further control when jobs in your workflow will run. For example, this workflow will run when a review is requested on a pull request, but the specific_review_requested job will only run when a review by octo-team is requested.

```yaml
on:
  pull_request:
    types: [review_requested]
jobs:
  specific_review_requested:
    runs-on: ubuntu-latest
    if: ${{ github.event.requested_team.name == 'octo-team'}}
    steps:
      - run: echo 'A review from octo-team was requested'
```

#### Running your `pull_request` workflow based on the head or base branch of a pull request

You can use the `branches` or `branches-ignore` filter to configure your workflow to only run on pull requests that target specific branches.

For example, this workflow will run when someone opens a pull request that targets a branch whose name starts with `releases/`:

```yaml
on:
  pull_request:
    types:
      - opened
    branches:
      - 'releases/**'
```

>[!NOTE]
>  It's same like `push` event.


#### Running your pull_request workflow when a pull request merges

When a pull request merges, the pull request is automatically closed. 

To run a workflow when a pull request merges, use the `pull_request` `closed` event type along with a conditional that checks the merged value of the event.

For example, the following workflow will run whenever a pull request closes. The `if_merged` job will only run if the pull request was also merged.

```yaml
on:
  pull_request:
    types:
      - closed

jobs:
  if_merged:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
    - run: |
        echo The PR was merged
```


## Contexts & Expressions

### Literals Expressions

As part of an expression, you can use `boolean`, `null`, `number`, or `string` data types.

| Data type |                           **Literal value**                                                        |
|---------- |----------------------------------------------------------------------------------------------------|
| boolean   |                      true or false                                                                 |
|  null     |                            null                                                                    |
| number    |                Any number format supported by JSON.                                                |
|string     | You don't need to enclose strings in ${{ and }}. However, if you do, you must use single quotes (') around the string. To use a literal single quote, escape the literal single quote using an additional single quote (''). Wrapping with double quotes (") will throw an error. |

**Example of literals:**

```yaml
env:
  myNull: ${{ null }}
  myBoolean: ${{ false }}
  myIntegerNumber: ${{ 711 }}
  myFloatNumber: ${{ -9.2 }}
  myHexNumber: ${{ 0xff }}
  myExponentialNumber: ${{ -2.99e-2 }}
  myString: Mona the Octocat
  myStringInBraces: ${{ 'It''s open source!' }}
```

### Operators Expressions


| Operator |                           Description                                                       |
|---------- |----------------------------------------------------------------------------------------------------|
| `( )`   |                     Logical grouping                                                            |
|  `[ ]`     |                            Index                                                                    |
| ` . `    |              	Property de-reference                                              |
| `!`     |	                       Not |
| ` < `   |   Less than

### Github Context

The `github` context contains information about the workflow run and the event that triggered the run. 

```yaml
name: Run CI
on: [push, pull_request]

jobs:
  normal_ci:
    runs-on: ubuntu-latest
    steps:
      - name: Run normal CI
        run: echo "Running normal CI"

  pull_request_ci:
    runs-on: ubuntu-latest
    if: ${{ github.event_name == 'pull_request' }}
    steps:
      - name: Run PR CI
        run: echo "Running PR only CI"
```



### secrets context

The secrets context contains the names and values of secrets that are available to a workflow run. 

The secrets context is not available for composite actions due to security reasons. 

If you want to pass a secret to a composite action, you need to do it explicitly as an input. 

`GITHUB_TOKEN` is a secret that is automatically created for every workflow run, and is always included in the `secrets` context


 
