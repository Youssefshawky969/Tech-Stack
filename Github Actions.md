### Workflow Syntax:
- `name`

 This is the name of the workflow. GitHub displays the names of your workflows under your repository's "Actions" tab. If you omit name, GitHub displays the workflow             file path relative to the root of the repository.

  

- `on`

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

- `jobs`

  A workflow run is made up of one or more jobs, which run in parallel by default.

  To run jobs sequentially, you can define dependencies on other jobs using the `jobs.<job_id>.needs` keyword.

  Each job runs in a runner environment specified by `runs-on`.

  Use `jobs.<job_id>` to give your job a unique identifier.

  The key job_id is a string and its value is a map of the job's configuration data. You must replace <job_id> with a string that is unique to the jobs object.

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

    - Use `jobs.<job_id>.name`

  to set a name for the job, which is displayed in the GitHub UI.

    - Use `jobs.<job_id>.needs`

  to identify any jobs that must complete successfully before this job will run.

  It can be a string or array of strings.

   If a job fails or is skipped, all jobs that need it are skipped unless the jobs use a conditional expression that causes the job to continue. If a run contains a series of jobs that need each other, a failure or skip applies to all jobs in the dependency chain from the point of failure or skip onwards.

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


