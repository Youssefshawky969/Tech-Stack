## Infrastructure as Code

### What is Infrastructure as Code with Terraform?

Infrastructure as Code (IaC) tools allow you to manage infrastructure with configuration files.

 IaC allows you to build, change, and manage your infrastructure in a safe, consistent, and repeatable way by defining resource configurations that you can version, reuse, and share.

 Terraform is HashiCorp's infrastructure as code tool.

 It lets you define resources and infrastructure in human-readable, declarative configuration files, and manages your infrastructure's lifecycle.

 Using Terraform has several advantages over manually managing your infrastructure:
 - Terraform can manage infrastructure on multiple cloud platforms.
 - The human-readable configuration language helps you write infrastructure code quickly.
 - Terraform's state allows you to track resource changes throughout your deployments.
 - You can commit your configurations to version control (Git) to safely collaborate on infrastructure.

### manage any infrastrcture

Terraform plugins called providers let Terraform interact with cloud platforms and other services via their application programming interfaces (APIs).

HashiCorp and the Terraform community have written over 1,000 providers to manage resources on Amazon Web Services (AWS), Azure, Google Cloud Platform (GCP), Kubernetes, Helm, GitHub.

### Standardize your deployment workflow

Providers define individual units of infrastructure, for example compute instances or private networks, as resources.

You can compose resources from different providers into reusable Terraform configurations called modules, and manage them with a consistent language and workflow.

Terraform's configuration language is declarative, meaning that it describes the desired end-state for your infrastructure, in contrast to procedural programming languages that require step-by-step instructions to perform tasks.

Terraform providers automatically calculate dependencies between resources to create or destroy them in the correct order.

### Track your infrastructure

Terraform keeps track of your real infrastructure in a state file, which acts as a source of truth for your environment. Terraform uses the state file to determine the changes to make to your infrastructure so that it will match your configuration.

### Collaborate

Terraform allows you to collaborate on your infrastructure with its remote state backends.

When you use HCP Terraform (free for up to five users), you can securely share your state with your teammates, provide a stable environment for Terraform to run in, and prevent race conditions when multiple people make configuration changes at once.

You can also connect HCP Terraform to version control systems (VCSs) like GitHub, GitLab, and others, allowing it to automatically propose infrastructure changes when you commit configuration changes to VCS. 

This lets you manage changes to your infrastructure through version control, as you would with application code.

## Create Infrastrucre

### Write Configuration

Terraform configuration files are plain text files in HashiCorp's configuration language, HCL, with file names ending with `.tf`.

When you perform operations with the Terraform CLI, Terraform loads all of the configuration files in the current working directory and automatically resolves dependencies within your configuration.

This allows you to organize your configuration into multiple files and in any order you choose.

Terraform configuration is organized into a few types of blocks that let you configure 
- Terraform itself
- Terraform providers
- and the resources
- and data sources

  that make up your infrastructure.


Create a new directory for the Terraform configuration

```bash
mkdir learn-terraform-get-started-aws
```

Change into the directory.

```bash
cd learn-terraform-get-started-aws
```

#### `terraform` block

The `terraform {}` block configures Terraform itself 
- including which providers to install
- and which version of Terraform to use to provision your infrastructure.

Using a consistent file structure makes maintaining your Terraform projects easier, so we recommend configuring your Terraform block in a dedicated `terraform.tf` file.

Create and open a new file named `terraform.tf` with the following configuration to define your Terraform block.

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  }

  required_version = ">= 1.2"
}
```

Terraform uses binary plugins called providers to manage your resources by calling your cloud provider's APIs.

Terraform providers are distributed and versioned separately from Terraform.

By decoupling providers from the Terraform binary, Terraform can support any infrastructure vendor with an API.

The `required_providers` block lets you set version constraints on the providers your configuration uses.

>[!NOTE]
> HashiCorp maintains the Terraform Registry, from which you can source public Terraform providers and modules.

Set `source` and `version` arguments for each provider in the `required_providers` block.

The source argument specifies a hostname (optional), namespace, and provider name. 

In the example configuration, the `aws` provider's source is `hashicorp/aws`, which is a shortened form of `registry.terraform.io/hashicorp/aws`, the address of the provider in the Terraform Registry.

The version argument sets a version constraint for your AWS provider.

If you do not specify a version constraint, Terraform defaults to the most recent version of the provider.

We recommend using version constraints to ensure that Terraform does not install a version of the provider that you have not tested with your configuration.

The string `~> 5.92` means your configuration supports any version of the provider with a major version of `5` and a minor version greater than or equal to `92`

The example configuration also defines the required version of Terraform, itself. 

The string `>= 1.2` means your configuration supports any version of Terraform greater than or equal to `1.2`.


#### Configuration blocks

paste the configuration below into a new file named `main.tf`.

```hcl
provider "aws" {
  region = "us-west-2"
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "app_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"

  tags = {
    Name = "learn-terraform"
  }
}
```

When you write a new Terraform configuration, hashicorp recommend defining your provider blocks and other primary infrastructure in `main.tf` as a best practice.

> [!NOTE]
> As you add to your configuration, you may choose to organize related infrastructure into different files.

##### Providers

The `provider` block configures options that apply to all resources managed by your provider, such as the region to create them in.

This `provider` block configures the aws provider. 

The label of the provider block corresponds to the name of the provider in the `required_providers` list in your `terraform` block.

```hcl
provider "aws" {
  region = "us-west-2"
}
```

You can use multiple provider blocks in your Terraform configuration to configure multiple providers or multiple instances of the same provider with different configurations, such as a different region.

Terraform providers must authenticate with your cloud provider's API to manage your resources.


> [!NOTE]
>
> Providers often support multiple authentication methods.
> 
> Terraform's AWS provider uses the same authentication methods as the AWS CLI.
>
> If you have not already done so, configure your AWS credentials as environment variables in your terminal.


To use your IAM credentials to authenticate the Terraform AWS provider, set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

```bash
$ export AWS_ACCESS_KEY_ID=
$ export AWS_SECRET_ACCESS_KEY=
```

You can use the AWS CLI to verify your credentials.

```bash
$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************ZJZK              env
secret_key     ****************St8S              env
    region                <not set>             None    None
```

##### Data sources

You can use `data` blocks to query your cloud provider for information about other resources.

This data source fetches data about the latest AWS AMI that matches the filter, so you do not have to hardcode the AMI ID into your configuration.

Data sources help keep your configuration dynamic and avoid hardcoded values that can become stale.

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  owners = ["099720109477"] # Canonical
}
```

Data sources have an ID, which you can use to reference the data attributes within your configuration.

Data source IDs are prefixed with data, followed by the block's type and name.

In this example, the `data.aws_ami.ubuntu` data source loads an AMI for the most recent Ubuntu Noble Numbat release in the region configured for your provider.


##### Resources

A `resource` block defines components of your infrastructure.

The example configuration defines a resource block to create an AWS EC2 instance.

```hcl
resource "aws_instance" "app_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"

  tags = {
    Name = "learn-terraform"
  }
}
```

Provider developers determine supported resources types and their arguments.

The first line of a `resource` block declares a **resource type** and **resource name**.

In this example, the resource type is `aws_instance`.

The prefix of the resource type corresponds to the name of the provider, and the rest of the string is the provider-defined resource type.

 Together, the resource type and resource name form a unique **resource address** for the resource in your configuration.

 The resource address for your EC2 instance is `aws_instance.app_server`.

 You can refer to a resource in other parts of your configuration by its resource address.

 The arguments in your `resource` block configure the resource and its behavior:

 - The `ami` argument specifies which machine image to use by referencing your `data.aws_ami.ubuntu` data source's `id` attribute.
 - The `instance_type` argument hardcodes `t2.micro` as the type, which qualifies for the AWS free tier.
 - The tags argument sets the EC2 instance's name. You can also set other tags for your EC2 instance in the tags argument.


#### Format configuration

HashiCorp recommend using consistent formatting to ensure readability. The terraform fmt command automatically reformats all configuration files in the current directory according to HashiCorp's recommended style.


```bash
$ terraform fmt
```

#### Initialize your workspace

Before you can apply your configuration, you must initialize your Terraform workspace with the terraform `init command`.

As part of initialization, Terraform downloads and installs the providers defined in your configuration in your current working directory.

Initialize your Terraform workspace.
```bash
$ terraform init

Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 5.92"...
- Installing hashicorp/aws v5.98.0...
- Installed hashicorp/aws v5.98.0 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

Terraform downloaded the `aws` provider and installed it in a hidden `.terraform` subdirectory of your current working directory.

Terraform also created a file named `.terraform.lock.hcl` which specifies the exact provider versions used with your workspace, ensuring consistency between runs.

#### Validate configuration

Make sure your configuration is syntactically valid and internally consistent by using the `terraform validate` command.

```bash
$ terraform validate

Success! The configuration is valid.
```
The example configuration provided above is valid, so Terraform returns a success message.

The validate command helps you identify errors in your configuration. For example, if you mistype a resource name or refer to an argument your resource does not support, Terraform will report an error when you validate your configuration.

#### Create infrastructure (Apply)

Terraform makes changes to your infrastructure in two steps.

Terraform creates an execution plan for the changes it will make. 

Review this plan to ensure that Terraform will make the changes you expect.

Once you approve the execution plan, Terraform applies those changes using your workspace's providers.

This workflow ensures that you can detect and resolve any unexpected problems with your configuration before Terraform makes changes to your infrastructure.

Plan and apply your configuration now with the `terraform apply` command.

Terraform will print out the execution plan and ask you to confirm the changes before it applies them.

Your configuration includes a single resource, `aws_instance.app_server`, so your plan will indicate that Terraform will create your EC2 instance.

```bash
$ terraform apply

data.aws_ami.ubuntu: Reading...
data.aws_ami.ubuntu: Read complete after 1s [id=ami-0026a04369a3093cc]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.app_server will be created
  + resource "aws_instance" "app_server" {
      + ami                                  = "ami-0026a04369a3093cc"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + enable_primary_ipv6                  = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + iam_instance_profile                 = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_lifecycle                   = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + spot_instance_request_id             = (known after apply)
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "learn-terraform"
        }
      + tags_all                             = {
          + "Name" = "learn-terraform"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification (known after apply)

      + cpu_options (known after apply)

      + ebs_block_device (known after apply)

      + enclave_options (known after apply)

      + ephemeral_block_device (known after apply)

      + instance_market_options (known after apply)

      + maintenance_options (known after apply)

      + metadata_options (known after apply)

      + network_interface (known after apply)

      + private_dns_name_options (known after apply)

      + root_block_device (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

The output format is similar to the diff format generated by tools such as Git.

The `+` next to `resource "aws_instance" "app_server"` means that when you apply this plan, Terraform will create the resource with `aws_instance.app_server` as its ID.

Terraform shows the attributes that will be set on your EC2 instance and indicates that some values will be `(known after apply)`.

Terraform has not created any infrastructure yet.

If the plan showed unexpected changes, you could cancel the operation before completing the apply step.

In this case the plan is acceptable, so type `yes` at the confirmation prompt to proceed. Applying your plan will take a few minutes.

```bash
  Enter a value: yes

aws_instance.app_server: Creating...
aws_instance.app_server: Still creating... [10s elapsed]
aws_instance.app_server: Creation complete after 14s [id=i-0c636e158c30e48f9]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

You have now created infrastructure using Terraform. Visit the EC2 console and find your new EC2 instance.

#### Inspect state

When you applied your configuration, Terraform wrote data about your infrastructure into a file called `terraform.tfstate`.

Terraform stores data about your infrastructure in its state file, which it uses to manage resources over their lifecycle.

List the resources and data sources in your Terraform workspace's state with the `terraform state list` command.

```bash
$ terraform state list

data.aws_ami.ubuntu
aws_instance.app_server
```

Even though the data source is not an actual resource, Terraform tracks it in your state file.

Print out your workspace's entire state using the `terraform show` command.

```bash
$ terraform show

# data.aws_ami.ubuntu:
data "aws_ami" "ubuntu" {
    architecture          = "x86_64"
    arn                   = "arn:aws:ec2:us-west-2::image/ami-0026a04369a3093cc"
    block_device_mappings = [
        {
            device_name  = "/dev/sda1"
            ebs          = {
                "delete_on_termination" = "true"
                "encrypted"             = "false"
                "iops"                  = "0"
                "snapshot_id"           = "snap-051c478203945e90f"
                "throughput"            = "0"
                "volume_size"           = "8"
                "volume_type"           = "gp3"
            }

## ...

    }
}
```



When you use Terraform to plan and apply changes to your workspace's infrastructure, Terraform compares 
- the last known state in your state file
- your current configuration
- and data returned by your providers

  to create its execution plan.

Your state file can include sensitive information about your infrastructure, such as passwords or security keys, so you must store your state file securely and restrict access to only those who need to manage your infrastructure with Terraform.

By default, Terraform creates your state file locally.

As your infrastructure operations mature, storing your state remotely using HCP Terraform will let you collaborate with your team more easily and keep your state file secure.












