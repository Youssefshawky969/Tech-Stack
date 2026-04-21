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




## Variables and outputs

Input variables let you parametrize the behavior of your Terraform configuration.

You can also define output values to expose data about the resources you create.

Variables and outputs also allow you to integrate your Terraform workspaces with other automation tools by providing a consistent interface to configure and retrieve data about your workspace's infrastructure.

### Input Variables

Create a new file in your learn-terraform-aws-get-started directory named `variables.tf` with the following configuration.

```hcl
variable "instance_name" {
  description = "Value of the EC2 instance's Name tag."
  type        = string
  default     = "learn-terraform"
}

variable "instance_type" {
  description = "The EC2 instance's type."
  type        = string
  default     = "t2.micro"
}
```

These input variables allow you to update the EC2 instance's name and type without modifying your configuration files each time.

Both variables set a default value for Terraform to use if you do not specify a value for them.

Terraform recommend that you put your workspace's variable and output definitions in their own respective files, `variables.tf` and `outputs.tf`, to make it easier for users to maintain your Terraform configuration.

Update the instance configuration in `main.tf` to refer to these variables instead of hard-coding the argument values.

```hcl
resource "aws_instance" "app_server" {
   ami           = data.aws_ami.ubuntu.id
 - instance_type = "t2.micro"
 + instance_type = var.instance_type

  tags = {
  - Name = "learn-terraform"
  + Name = var.instance_name
  }
}
```
You can set values for your Terraform variables in a number of ways, including environment variables, command line arguments, and in files stored on disk.

Run a Terraform plan without applying it to see what would happen if you changed your EC2 instance type from `t2.micro` to `t2.large` using a command line variable.

```bash
$ terraform plan -var instance_type=t2.large

data.aws_ami.ubuntu: Reading...
data.aws_ami.ubuntu: Read complete after 1s [id=ami-0026a04369a3093cc]
aws_instance.app_server: Refreshing state... [id=i-0c636e158c30e48f9]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # aws_instance.app_server will be updated in-place
  ~ resource "aws_instance" "app_server" {
        id                                   = "i-0c636e158c30e48f9"
      ~ instance_type                        = "t2.micro" -> "t2.large"
      ~ public_dns                           = "ec2-34-216-162-36.us-west-2.compute.amazonaws.com" -> (known after apply)
      ~ public_ip                            = "34.216.162.36" -> (known after apply)
        tags                                 = {
            "Name" = "learn-terraform"
        }
        # (36 unchanged attributes hidden)

        # (8 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply"
now.
```

If you were to apply this plan, Terraform would update your EC2 instance with the new instance type.

Terraform needs to replace the instance to implement this change, so the AWS provider also indicates that the IP address and hostname will change as well, but marks them as (`known after apply`) because AWS will not assign the new values until you apply the change to recreate the instance.

## Output values

Output values allow you to access attributes from your Terraform configuration and consume their values with other automation tools or workflows.

Create a new file named `outputs.tf` with the following configuration.

```hcl
output "instance_hostname" {
  description = "Private DNS name of the EC2 instance."
  value       = aws_instance.app_server.private_dns
}
```

This output value exposes your EC2 instance's hostname from your Terraform workspace.

Apply your configuration. Since the default values of the two variables you created are the same as the hard-coded values they replaced, Terraform will detect that the only change is the output value you added. Respond to the confirmation prompt with a `yes` to add the output value to your workspace.

```bash
$ terraform apply
data.aws_ami.ubuntu: Reading...
data.aws_ami.ubuntu: Read complete after 1s [id=ami-0026a04369a3093cc]
aws_instance.app_server: Refreshing state... [id=i-0c636e158c30e48f9]

Changes to Outputs:
  + instance_hostname = "ip-172-31-35-26.us-west-2.compute.internal"

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

instance_hostname = "ip-172-31-35-26.us-west-2.compute.internal"
```

Terraform prints out your output values when you run a plan or apply, and also stores them in your workspace's state file.

Review your output values using the `terraform output` command.

```bash
$ terraform output
instance_hostname = "ip-172-31-35-26.us-west-2.compute.internal"
```

## Modules

Modules are reusable sets of configuration

Use modules to consistently manage complex infrastructure deployments that include multiple resources and data sources.

Like providers, you can source modules from the Terraform Registry. You can also create your own modules and share them within your organization.

### Module block

Add a module block to your configuration in main.tf to create a VPC and related networking resources for your EC2 instance.

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.19.0"

  name = "example-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24"]

  enable_dns_hostnames    = true
}
```
Since Terraform automatically resolves dependencies within your configuration, you can organize your configuration blocks in any order you like.

As a best practice, terraform recommend that you organize your configuration so that it is easy for you and your team to maintain.

This configuration defines a VPC named example-vpc with one public and two private subnets.

Move your EC2 instance into your new VPC by updating the resource block to match the one below.

```hcl
resource "aws_instance" "app_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  vpc_security_group_ids = [module.vpc.default_security_group_id]
  subnet_id              = module.vpc.private_subnets[0]

  tags = {
    Name = var.instance_name
  }
}
```

This change will configure your EC2 instance to be in one of your new VPC's public subnets and use its default security group.

Whenever you add a new module to your configuration, you will need to install it by re-initializing the workspace.

Install the VPC module by running `terraform init`.

```bash
$ terraform init
Initializing the backend...
Initializing modules...
Downloading registry.terraform.io/terraform-aws-modules/vpc/aws 5.19.0 for vpc...
- vpc in .terraform/modules/vpc
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/aws v5.98.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

When you initialize an existing workspace, Terraform detects and installs any new providers and modules.

Terraform tracks the current versions of the providers used with your configuration in the `.terraform.lock.hcl` file in your workspace's directory.

