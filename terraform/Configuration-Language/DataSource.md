
Terraform data sources let you dynamically fetch data from APIs or other Terraform state backends.

Examples of data sources include machine image IDs from a cloud provider or Terraform outputs from other configurations. Data sources make your configuration more flexible and dynamic and let you reference values from other configurations, helping you scope your configuration while still referencing any dependent resource attributes.

In HCP Terraform, data sources let you share data between workspaces.

The VPC configuration uses a variable called `aws_region` with a default value of `us-east-1` to set the region. 
However, changing the value of the `aws_region` variable will not successfully change the region because the VPC configuration includes an `azs` argument to set Availability Zones, which is a hard-coded list of availability zones in the `us-east-1` region.

```hcl
module "vpc" {
##...
  azs             = ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e"]
##...
}
```

Use the `aws_availability_zones` data source to load the available AZs for the current region. 

Add the following to `main.tf`.
```hcl
data "aws_availability_zones" "available" {
  state = "available"

  filter {
    name   = "zone-type"
    values = ["availability-zone"]
  }
}
```

The aws_availability_zones data source is part of the AWS provider and retrieves a list of availability zones based on the arguments supplied.

In this case, the `state` argument limits the availability zones to only those that are currently available.

You can reference data source attributes with the pattern `data.<NAME>.<ATTRIBUTE>`.

Update the VPC configuration to use this data source to set the list of availability zones.
```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.0"

  cidr = var.vpc_cidr_block

  azs             = data.aws_availability_zones.available.names
  private_subnets = slice(var.private_subnet_cidr_blocks, 0, 2)
  public_subnets  = slice(var.public_subnet_cidr_blocks, 0, 2)

##...
}
```

Configure the VPC workspace to output the region, which the application workspace will require as an input. Add a data source to `main.tf` to access region information.

```hcl
data "aws_region" "current" { }
```

Add an output for the region to `outputs.tf`.
```hcl
output "aws_region" {
  description = "AWS region"
  value       = data.aws_region.current.name
}
```


