[section:introduction]

### Introduction
CircleCI is one of the most powerful and flexible CI/CD platforms used by modern software teams to automate building, testing, and deploying applications.
It provides highly scalable pipelines, modular configuration patterns, and deep integration with version control systems such as GitHub, GitLab, and Bitbucket.
This document provides a full, comprehensive deep dive into CircleCI’s architecture and concepts with examples for every core component.
It is designed to take you from foundational understanding to expert-level mastery.

[section:overview]

### Overview

CircleCI organizes all automation into Pipelines → Workflows → Jobs → Steps executed inside isolated Executors.
Workspaces, caches, and artifacts enable data movement and optimization, while reusable components and orbs simplify configuration.
CircleCI executes your config by converting it into a Directed Acyclic Graph (DAG), ensuring optimized, parallel, and reliable CI/CD operations. The following sections break down every CircleCI concept in professional detail—with examples.

[section:pipline]

### Pipelines

A pipeline in CircleCI is the top-level unit of execution that begins when CircleCI is triggered by an external event, such as a Git push, pull request, tag creation, scheduled cron job, or direct API call. When a pipeline starts, CircleCI retrieves the latest commit metadata, loads and parses the `.circleci/config.yml` file, resolves pipeline-level parameters, applies workspace, environment, and context rules, and constructs an internal Directed Acyclic Graph (DAG) representing workflows and jobs. A pipeline can contain multiple workflows, each with its own orchestration logic. During execution, CircleCI provisions environments for each job, runs associated steps, manages caching, workspaces, and artifacts, and updates the workflow state based on job results. The pipeline ends once all workflows have succeeded or failed, and the result is sent back to the version control system. CircleCI also supports dynamic configuration, where an initial minimal config triggers a setup workflow that generates a second full configuration at runtime, enabling monorepo strategies and conditional pipeline generation.

Example:
A pipeline triggered automatically when pushing to GitHub:
```
version: 2.1
workflows:
pipeline_example:
jobs:
- build
jobs:
build:
docker:
- image: cimg/base:stable
steps:
- checkout
- run: echo "This pipeline started from a new commit!"
```

[section:configuration file structure]
### Configuration File Structure

The `config.yml` file defines every aspect of pipeline behavior. It contains top-level sections including `version`, `orbs`, `executors`, `commands`, `jobs`, and `workflows`, each serving a distinct purpose within CircleCI's configuration model. The file is parsed and validated strictly according to CircleCI’s schema. The structure supports extensibility through reusable components and parameterization. The `version` tag sets the configuration syntax version, typically `2.1`, enabling advanced features like orbs and pipeline parameters. The `orbs` key imports external configurations; `executors` define reusable runtime environments; `commands` encapsulate reusable sets of steps; `jobs` define units of work; and `workflows` describe orchestration logic. CircleCI processes this file before beginning pipeline execution, expanding parameters, orbs, and reusable elements into a unified internal representation.

Example:
```
version: 2.1
jobs:
hello:
docker:
- image: cimg/base:stable
steps:
- run: echo "Hello CircleCI"
workflows:
main:
jobs:
- hello
```

[section:workflow]
### Workflow

Workflows define how jobs are orchestrated within a pipeline. They establish the execution order, dependencies, concurrency, conditional behavior, and scheduling rules for all jobs. Internally, CircleCI constructs a Directed Acyclic Graph, where nodes represent jobs and edges represent dependency relationships defined with the `requires`: keyword. Jobs can run sequentially, in parallel, conditionally based on branches or tags, or according to scheduled cron expressions. Workflows support advanced behaviors such as approval jobs that pause execution pending manual confirmation, and matrix workflows that automatically expand a job template into multiple parallel variations (e.g., testing across different programming language versions). Through workflows, CircleCI optimizes resource usage, organizes pipelines into modular phases, and provides fine-grained control over how and when jobs are executed.

Example:
A workflow that runs `build` first, then `test`, then runs `deploy` only on the main branch:
```
workflows:
  ci_pipeline:
    jobs:
      - build
      - test:
          requires:
            - build
      - deploy:
          requires:
            - test
          filters:
            branches:
               only: main
```
[section:jobs]
### Jobs

A job is an isolated unit of work consisting of defined steps executed inside a selected executor environment. Each job starts with a clean state and does not share filesystem data with other jobs unless explicitly managed using workspaces. A job includes environment variables, resource configuration, shell settings, and the series of steps that will run in order. During execution, CircleCI provisions the executor, injects environment variables and contexts, executes steps one-by-one, and handles persistence mechanisms such as caches, artifacts, and workspaces. Jobs fail if any step returns a non-zero exit code unless error handling is adjusted using conditional directives. Jobs can be parameterized, allowing a single job definition to support multiple configurations, and can be used within matrix workflows to scale testing across multiple environments.

Example:
A job that installs dependencies and runs tests:
```
jobs:
  test_app:
    docker:
      - image: cimg/python:3.11
    steps:
      - checkout
      - run: pip install -r requirements.txt
      - run: pytest
```
[section:steps]
### Steps

Steps are the individual actions executed within a job. They include built-in CircleCI steps such as `checkout`, which retrieves the repository; `restore_cache` and `save_cache` for caching; `persist_to_workspace` and `attach_workspace` for inter-job data sharing; and `store_artifacts` for uploading outputs. Additionally, the `run` step executes custom shell commands. Steps execute sequentially and inherit the job’s shell environment. If a step fails, the job fails unless otherwise configured. CircleCI streams step logs to the user interface, enabling granular debugging. Steps can reference parameters, use bash conditionals, and invoke reusable commands. Steps provide the execution-level directives that bring each job to life.

Example:
```
steps:
  - checkout
  - run: echo "Starting build..."
  - run: make build
  - store_artifacts:
      path: results/
```
[section:executors]

### Executors

Executors define the environment where a job runs. CircleCI supports several executor types: Docker, Machine, macOS, Windows, and Remote Docker. The Docker executor runs jobs inside lightweight containers for fast execution and supports supplemental service containers such as databases. The Machine executor provisions a full virtual machine suitable for Docker-in-Docker operations, privileged operations, and virtualization tasks. macOS executors run macOS VMs for iOS and Swift builds, while Windows executors run Windows Server environments. Remote Docker provides a separate Docker environment dedicated to building Docker images. Executors ensure that each job runs in a consistent, isolated environment with controlled resources, CPU, and memory. They define the foundational context in which all steps will execute.

Examples:
Docker executor for Node.js
```
executors:
  node_executor:
    docker:
      - image: cimg/node:20.0


jobs:
  build:
    executor: node_executor
    steps:
      - checkout
      - run: npm install
      - run: npm run build
```

[section:commands]
### Commands
Commands in CircleCI are reusable groups of steps designed to encapsulate frequently repeated logic. They function similarly to functions in programming languages, providing parameters and step encapsulation. Commands reduce duplication and enable consistent patterns across multiple jobs and workflows. Defined under the `commands` section of the config, they accept parameters and are expanded inline when invoked. Commands improve readability, maintainability, and modularity of complex CI/CD pipelines.

Example:
```
commands:
  install_deps:
    steps:
      - run: pip install -r requirements.txt


jobs:
  test:
    docker:
      - image: cimg/python:3.11
    steps:
      - checkout
      - install_deps
      - run: pytes
```
[section:parameters]

### Parameters
Parameters enable dynamic and reusable configuration in CircleCI. They can be applied to commands, executors, jobs, and workflows, allowing a single definition to support multiple variations of behavior. Parameters may be strings, booleans, integers, enums, lists, or complex types depending on use case. CircleCI resolves parameters at config-processing time before constructing the workflow DAG, ensuring that job expansions (such as those in matrix workflows) occur fully before execution. Parameters significantly increase the flexibility and scalability of CircleCI configurations.

Example:
```
jobs:
  test:
    parameters:
      py_ver:
        type: string
    docker:
      - image: cimg/python:<< parameters.py_ver >>
    steps:
      - checkout
      - run: python --version


workflows:
  test_matrix:
    jobs:
      - test:
          py_ver: "3.9"
      - test:
          py_ver: "3.11"
```

[section:reusable components]
### Reusable Components
CircleCI’s reusable component model includes commands, jobs, and executors. These allow pipeline authors to modularize logic and avoid duplication. Reusable commands group repeated steps; reusable executors provide consistent environments; reusable jobs define templates that can be invoked with different parameters. Using reusable components results in more concise, maintainable, and extensible CI/CD configurations, especially in large or multi-project environments.

Example:
```
jobs:
  base_job:
    parameters:
      message:
        type: string
    docker:
      - image: cimg/base:stable
    steps:
      - run: echo << parameters.message >>
```

[section:orbs]
### Orbs
Orbs are versioned, shareable packages of CircleCI configuration published to the Orb Registry. An orb may include reusable jobs, commands, executors, examples, and documentation, providing turnkey integrations for cloud services, programming languages, deployment platforms, and more. CircleCI expands orbs during configuration processing before validating workflows and jobs. Official, partner, and community orbs provide a powerful way to incorporate best practices and reduce boilerplate. Orbs support parameters, enabling wide customization while maintaining a succinct configuration.

Example:
AWS ECR orb
```
orbs:
  aws-ecr: circleci/aws-ecr@8.2.1


workflows:
  deploy:
    jobs:
      - aws-ecr/build-and-push-image:
          account-url: AWS_ACCOUNT_URL
          repo: my-app
          tag: "latest"
```

[section:Environment variables and context]
### Environment variables and Context
Environment variables in CircleCI provide configuration settings and secrets required by jobs. They can be defined at multiple levels: project-level settings, job environment blocks, executor images, or injected through contexts. Contexts provide a secure mechanism for managing sensitive information across multiple projects within an organization. They support role-based access control, ensuring that only authorized users and pipelines can access sensitive variables. CircleCI injects environment variables into the job’s runtime environment before steps execute, ensuring secure and consistent access throughout the workflow.

Example:
Using a context named production-secrets:
```
workflows:
  deploy_workflow:
    jobs:
      - deploy:
          context: production-secrets
```

[section:caching]
### Caching
Caching in CircleCI accelerates pipelines by preserving directories or files between pipeline runs. Cache keys determine whether a cache will be restored, using strategies such as exact match or prefix matching. Caches are typically used for dependency directories—such as Python packages, Node modules, or compiled assets—and can significantly reduce execution time. Caches persist across pipelines but are isolated from workspaces, which are used only within a single workflow. Proper key design is crucial for effective caching, balancing between cache hit rate and correctness.
Example:
```
steps:
  - restore_cache:
      keys:
        - v1-pip-{{ checksum "requirements.txt" }}
  - run: pip install -r requirements.txt
  - save_cache:
      key: v1-pip-{{ checksum "requirements.txt" }}
      paths:
        - ~/.cache/pip
```

[section:workspaces]
### Workspaces
Workspaces provide a mechanism for sharing data between jobs within the same workflow. Unlike caches, workspaces persist only for the duration of a single workflow and are designed for passing build outputs, intermediate artifacts, or test binaries between sequential jobs. Workspaces support large files and maintain directory structure. CircleCI stores the workspace after a job uses `persist_to_workspace` and makes it available to later jobs via `attach_workspace`. Workspaces make multi-stage pipelines—such as build → test → deploy—possible in distributed environments.

Example:
```
jobs:
  build:
    steps:
      - checkout
      - run: mkdir build && echo "data" > build/output.txt
      - persist_to_workspace:
          root: build
          paths:
            - output.txt


test:
  steps:
    - attach_workspace:
        at: /tmp/workspace
    - run: cat /tmp/workspace/output.txt
```

[section:Artifacts]
### Artifact
Artifacts are files saved from jobs for long-term access after pipeline completion. These may include logs, reports, binaries, screenshots, coverage reports, or deployment packages. Artifacts are uploaded during the `store_artifacts` step, preserved by CircleCI, and accessible via the CircleCI UI after workflow execution. Unlike caches or workspaces, artifacts are intended for review, debugging, auditing, or manual download rather than inter-job communication. Artifacts help provide transparency into pipeline outputs and facilitate troubleshooting

Example:
```
steps:
  - run: mkdir reports && echo "Report Data" > reports/report.txt
  - store_artifacts:
      path: reports/
      destination: test-results
```
