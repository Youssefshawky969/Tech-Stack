## [section:overview]
### Overview
Terraform is an Infrastructur as Code "IAC" tool by HashiCorp that lets you define, provision, and manage cloud infrastructure using configuration files.

you just describe what you want (Servers, storage, databases, etc..) and terraform handels the creation.

## [section:providers]
### providers
Providers tell terrafrom which cloud or platfrom to work with. For Example, AWS, Azure, GCP, and etc...

think of it as a plugin that connect terraform to a specific platfrom's API

Example:
```
provider "aws" {
  region = "us-east-1"
}

```
Here, terraform will manage infrastructre on AWS in the US-east-1 region.

## [section:resources]
### Resources
A resource is any piece of infrastructure you want to create provider's instances, Storage, VPCs, etc...

Example:

```
resource "aws_instance" "my_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```
This create an EC2 instance using the provider AMI and type

## [section:variables]
### Variable
Variables make your Terrafrom code reusable and flexible. Instead of hardcoding values, you just define them in variables and refrence them elsewhere

Example:
```
variable "instance_type" {
  default = "t2.micro"
}
```
You can use it in the resource file
```
resource "aws_instance" "my_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
}
```

## [section:state]
### State

Terraform kepps track of what it has created using a state file (terraform.tfstate).
It compres the real-world infrastucre with your configuration files to know what to add, change, or delete

Example:
* You create an EC2 instance --> Terraform records it in the state.
* So if you later change the instance typer for example in the code, terraform sees the difference and updates it.

###### Best Practice:
Store the state file remotley (e.g,, S3 backend or HCL cloud) when working in teams.

## [section:modules]
### Modules
Modules are reusable groups of terraform files.
They make it easy to organize and reuse infrastucture code (like functions in programming)

Example for the structure:
```
main.tf
variables.tf
modules/
 └── ec2/
     ├── main.tf
     ├── variables.tf
     └── outputs.tf
```
Example usage:
```
module "web_server" {
  source         = "./modules/ec2"
  instance_type  = "t3.micro"
  ami_id         = "ami-0c55b159cbfafe1f0"
}
```
So now, your main Teeraform project can reuse this EC2 module anywhere.

## [section:end)
### Simple full example
so at the end, the whole configuration should be like this:
In `provider.tf`
```
provider "aws" {
  region = "us-east-1"
}
```
In `variables.tf`
```
variable "instance_type" {
  default = "t2.micro"
}
```
In `main.tf`
```
resource "aws_instance" "demo_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
}
```
in `state.tf`
```
terraform {
  backend "s3" {
    bucket = "terraform-state-demo"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}
```

Run Commands:

- To initialize provider plugins
```
terraform init
```
- To show what will be created
```
terrafrom plan
```
- To create the infrastucre
```
terrafrom apply
```
- To Delete it
```
terrafrom destroy
```
