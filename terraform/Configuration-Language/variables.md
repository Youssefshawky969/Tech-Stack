# Variables

## Customize Terraform configuration with variables

Input variables make your Terraform configuration more flexible by defining values that your end users can assign to customize the configuration. 

They provide a consistent interface to change how a given configuration behaves.



### Parameterize your configuration

Variable declarations can appear anywhere in your configuration files. However, we recommend putting them into a separate file called `variables`.tf to make it easier for users to understand how they can customize the configuration.

To parameterize an argument with an input variable, you must first define the variable, then replace the hardcoded value with a reference to that variable in your configuration.

Add a block declaring a variable named `aws_region` to `variables.tf`.

```hcl
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}
```

Variable blocks have three optional arguments.
- **Description**: A short description to document the purpose of the variable.
- **Type**: The type of data contained in the variable.
- **Default**: The default value.

Terraform recommend setting a description and type for all variables, and setting a default value when practical.

If you do not set a default value for a variable, you must assign a value before Terraform can apply the configuration. Terraform does not support unassigned variables.

Variable values must be literal values, and cannot use computed values like resource attributes, expressions, or other variables.

 You can refer to variables in your configuration with `var.<variable_name>`.

 Edit the provider block in `main.tf` to use the new `aws_region` variable.
```hcl
 provider "aws" {
-  region  = "us-west-2"
+  region  = var.aws_region
 }
```

Add another declaration for the `vpc_cidr_block` variable to `variables.tf`.

```hcl
variable "vpc_cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}
```

Now, replace the hard-coded value for the VPC's CIDR block with a variable in `main.tf`.

```hcl
module "vpc" {
   source  = "terraform-aws-modules/vpc/aws"
   version = "5.7.0"

-  cidr = "10.0.0.0/16"
+  cidr = var.vpc_cidr_block
   ## ...
 }
```
Apply the updated configuration. Since the default values of these variables are the same as the hard-coded values they replaced, there will be no changes.

### Set the number of instances

Terraform supports several variable types in addition to `string`.

Use a `number` type to define the number of instances supported by this configuration. Add the following to `variables.tf`.

```hcl
variable "instance_count" {
  description = "Number of instances to provision."
  type        = number
  default     = 2
}
```
Update EC2 instances to use the instance_count variable in `main.tf`.

```hcl
 module "ec2_instances" {
   source = "./modules/aws-instance"

   depends_on = [module.vpc]

-  instance_count = 2
+  instance_count = var.instance_count
   ## ...
 }
```

When Terraform interprets values, either hard-coded or from variables, it will convert them into the correct type if possible.

So the instance_count variable would also work using a string (`"2"`) instead of a number (`2`).

We recommend using the most appropriate type in variable definitions to helps users of your configuration know the appropriate data type to use, as well as to catch configuration errors early.


### true/false values type

In addition to strings and numbers, Terraform supports several other variable types. A variable with type `bool` represents true/false values.

Use a `bool` type variable to control whether to configure a VPN gateway for your VPC. Add the following to `variables.tf`.

```hcl
variable "enable_vpn_gateway" {
  description = "Enable a VPN gateway in your VPC."
  type        = bool
  default     = false
}
```

Use this new variable in your VPC configuration by editing main.tf as follows.

```hcl
 module "vpc" {
   source  = "terraform-aws-modules/vpc/aws"
   version = "5.7.0"

   ## ...

   enable_nat_gateway = true
-  enable_vpn_gateway = false
+  enable_vpn_gateway = var.enable_vpn_gateway
   ## ...
 }

```

Leave the value for `enable_nat_gateway` hard-coded. In any configuration, there may be some values that you want to let users configure with variables and others you wish to hard-code.

When developing Terraform modules, you will often use variables to make the module's attributes configurable, to make the module more flexible.

In contrast, when writing Terraform configuration for a specific project, you may choose to hard-code attributes if you do not want to let users configure them.

### Multible values type

The variables you have used so far have all been single values.

Terraform calls these types of variables simple.

Terraform also supports collection variable types that contain more than one value.

- **List**: A sequence of values of the same type.
- **Map**: A lookup table, matching keys to values, all of the same type.
- **Set**: An unordered collection of unique values, all of the same type.

A likely place to use list variables is when setting the `private_subnets` and `public_subnets` arguments for the VPC.

Make this configuration easier to use and customizable by using lists and the `slice()` function.

Add the following variable declarations to `variables.tf`.

```hcl
variable "public_subnet_count" {
  description = "Number of public subnets."
  type        = number
  default     = 2
}

variable "private_subnet_count" {
  description = "Number of private subnets."
  type        = number
  default     = 2
}

variable "public_subnet_cidr_blocks" {
  description = "Available cidr blocks for public subnets."
  type        = list(string)
  default     = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24",
    "10.0.4.0/24",
    "10.0.5.0/24",
    "10.0.6.0/24",
    "10.0.7.0/24",
    "10.0.8.0/24",
  ]
}

variable "private_subnet_cidr_blocks" {
  description = "Available cidr blocks for private subnets."
  type        = list(string)
  default     = [
    "10.0.101.0/24",
    "10.0.102.0/24",
    "10.0.103.0/24",
    "10.0.104.0/24",
    "10.0.105.0/24",
    "10.0.106.0/24",
    "10.0.107.0/24",
    "10.0.108.0/24",
  ]
}
```

Notice that the type for the list variables is list(string). Each element in these lists must be a string.

List elements must all be the same type, but can be any type, including complex types like `list(list)` and `list(map)`.

Like lists and arrays used in most programming languages, you can refer to individual items in a list by index, starting with 0.

 Terraform also includes several functions that allow you to manipulate lists and other variable types.

Use the `slice()` function to get a subset of these lists.

The Terraform console command opens an interactive console that you can use to evaluate expressions in the context of your configuration. This can be very useful when working with and troubleshooting variable definitions.

Open a console with the `terraform console` command.

```bash
$ terraform console
>
```

Now use the Terraform console to inspect the list of private subnet blocks.

Refer to the variable by name to return the entire list.

```
var.private_subnet_cidr_blocks
tolist([
  "10.0.101.0/24",
  "10.0.102.0/24",
  "10.0.103.0/24",
  "10.0.104.0/24",
  "10.0.105.0/24",
  "10.0.106.0/24",
  "10.0.107.0/24",
  "10.0.108.0/24",
])
```

Retrieve the second element from the list by index with square brackets.

```
> var.private_subnet_cidr_blocks[1]
"10.0.102.0/24"
```

Now use the slice() function to return the first three elements from the list.

```
> slice(var.private_subnet_cidr_blocks, 0, 3)
tolist([
  "10.0.101.0/24",
  "10.0.102.0/24",
  "10.0.103.0/24",
])
```

The slice() function takes three arguments: the list to slice, the start index, and the end index (exclusive). It returns a new list with the specified elements copied ("sliced") from the original list.

Leave the console by typing `e.xit` or pressing `Control-D`.

```
> exit
```

Now update the VPC module configuration in `main.tf` to use the slice function to extract a subset of the CIDR block lists for your public and private subnet configuration.

```hcl
module "vpc" {
   source  = "terraform-aws-modules/vpc/aws"
   version = "5.7.0"

   cidr = var.vpc_cidr_block

   azs             = data.aws_availability_zones.available.names
- private_subnets = ["10.0.101.0/24", "10.0.102.0/24"]
- public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
+ private_subnets = slice(var.private_subnet_cidr_blocks, 0, var.private_subnet_count)
+ public_subnets  = slice(var.public_subnet_cidr_blocks, 0, var.public_subnet_count)
   ## ...
 }

```

This way, users of this configuration can specify the number of public and private subnets they want without worrying about defining CIDR blocks.

