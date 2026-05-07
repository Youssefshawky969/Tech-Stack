Terraform local values (or "locals") assign a name to an expression or value. 
Using locals simplifies your Terraform configuration – since you can reference the local multiple times, you reduce duplication in your code.

Locals can also help you write more readable configuration by using meaningful names rather than hard-coding values.

Unlike variables found in programming languages, Terraform's locals do not change values during or between Terraform runs such as plan, apply, or destroy. 
You can use locals to give a name to the result of any Terraform expression, and re-use that name throughout your configuration. 

Unlike input variables, locals are not set directly by users of your configuration.

## Use locals to name resources

In the configuration's `main.tf` file, several resource names consist of interpolations of the resource type and the `project` and `environment` values from the `resource_tags` variable.

Reduce duplication and simplify the configuration by setting the shared part of each `name` as a local value to re-use across your configuration.

First, define the local `name_suffix` by pasting the following snippet at the top of `main.tf`.

```hcl
locals {
  name_suffix = "${var.resource_tags["project"]}-${var.resource_tags["environment"]}"
}
```
As in any Terraform configuration, the order of your resource definitions and values does not affect how Terraform interprets them. To make your configuration more readable, consider putting local definitions near the top of your files.

Now, update the `name` attributes in the configuration to use this new local value.

```hcl
module "vpc" {
   source  = "terraform-aws-modules/vpc/aws"
   version = "2.66.0"

   name = "vpc-${local.name_suffix}"
   ## ...
 }

 module "app_security_group" {
   source  = "terraform-aws-modules/security-group/aws//modules/web"
   version = "3.17.0"

   name        = "web-sg-${local.name_suffix}"
   ## ...
 }

 module "lb_security_group" {
   source  = "terraform-aws-modules/security-group/aws//modules/web"
   version = "3.17.0"

   name        = "lb-sg-${local.name_suffix}"
   ## ...
 }

 module "elb_http" {
   source  = "terraform-aws-modules/elb/aws"
   version = "2.4.0"

   # Ensure load balancer name is unique
   name = "lb-${random_string.lb_id.result}-${local.name_suffix}"
   ## ...
 }
```

>[!NOTE]
>Note that the load balancer name includes a random string to ensure that it is unique, which is a requirement for AWS load balancer names.


## Combine variables with local values

Unlike variable values, local values can use dynamic expressions and resource arguments.

The resource_tags map in variables.tf defines the tags for the local name_suffix as defaults. A user could override the default value for this map and omit the project_name and environment tags.

Many projects require that all resources are tagged in a certain way to track them. To enforce this requirement, use a local value in combination with variables so the tags assigned to resources include at least the project name and environment.

Add the following new variable definitions to `variables.tf`.

```hcl
variable "project_name" {
  description = "Name of the project."
  type        = string
  default     = "my-project"
}

variable "environment" {
  description = "Name of the environment."
  type        = string
  default     = "dev"
}
```

Next, change the default value of the `resource_tags` variable to an empty map.

```hcl
 variable "resource_tags" {
   description = "Tags to set for all resources"
   type        = map(string)
   default     = { }
 }
```

Add a new `locals` block to `main.tf` to create a map combining both required tags and user defined tags.

```hcl
locals {
  required_tags = {
    project     = var.project_name,
    environment = var.environment
  }
  tags = merge(var.resource_tags, local.required_tags)
}
```
All of your configuration's local values can be defined in a single `locals` block, or you can use multiple blocks.

Update the definition of the `name_suffix` local to use the new variables for `project_name` and `environment`.

```hcl
locals {
  name_suffix = "${var.project_name}-${var.environment}"
}
```

