# AWS SDK using Pytohn

[section:overview]

### Overview
The AWS Software Development Kit (SDK) for Python, commonly known as Boto3, is the primary interface for programmatically interacting with Amazon Web Services. It enables developers and DevOps engineers to automate cloud operations, integrate AWS into applications, and manage infrastructure at scale.

Boto3 is built on top of Botocore, which handles authentication, request signing (SigV4), retries, and communication with AWS service APIs.
This document provides a full, in-depth overview of Boto3 concepts, interfaces, and usage patterns, with a focus on EC2 examples.

[section:how it works]

### How it works?

AWS services expose standardized, HTTPS-based JSON APIs, and Boto3 communicates with these APIs till reaches to AWS service Endpoint.

[section:componenets]

### Type of Calls

Boto3 exposes AWS services through four main interfaces:

**1- Client:** It provide a low-level and 1:1 mapping to AWS APIs and Detailed control, raw dictionary responses

**2- Resource:** Provide high-level, object-oriented abstraction and Clean, Pythonic operations

**3- Paginator:** It handles multi-page AWS API responses and Large listing operations

**4- Waiter:** Waits for state transitions of AWS resources and Asynchronous operations

Each serves a different purpose in automation and application development.

#### Boto3 Client Interface (Low-Level)

The client is the most direct representation of AWS APIs.
Each method corresponds exactly to an AWS operation.

Example:

- Create an EC2 Client
```
import boto3

ec2_client = boto3.client("ec2", region_name="us-east-1")
```

- Create EC2 instance
```
response = ec2_client.run_instances(
    ImageId="ami-0abc",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
)

instance_id = response["Instances"][0]["InstanceId"]
print(instance_id)
```

- Describe instances
```
response = ec2_client.describe_instances()
print(response)
```

#### Boto3 Resource Interface (High-Level, Pythonic)

The resource interface abstracts away low-level details and provides object-oriented models.

Example:
- Create an EC2 resource
```
import boto3

ec2 = boto3.resource("ec2")
```

- Listing EC2 instance
```
for instance in ec2.instances.all():
    print(instance.id, instance.state)
```

- Create an EC2 instance
```
instance = ec2.create_instances(
    ImageId="ami-12345",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
)[0]
```

#### Paginators (Handling Multi-Page API Responses)

A paginator is a tool that automatically handles multiple pages of responses from AWS API calls.

Many AWS API responses (like listing S3 objects) return limited results per call (e.g., 1000 objects max per page). If you have more, you get them in pages — and must retrieve the next page using a ContinuationToken.

Paginators automate this for you.

Example: 

```
paginator = ec2_client.get_paginator("describe_instances")

for page in paginator.paginate():
    print(page)
```

#### Waiters (Resource State Synchronization)

Many AWS operations are asynchronous. Waiters pause execution until the resource reaches a specific state.
it used in EC2 instance startup or stop, RDS instance availability, and CloudFormation stack completion.

Example:

```
waiter = ec2_client.get_waiter("instance_running")
waiter.wait(InstanceIds=["i-1234567890"])
```

#### Sessions (Multi-Account or Multi-Region Usage)

A Session controls credentials, regions, and profiles. used in Accessing multiple AWS accounts, Using temporary credentials, and Running automation scripts across regions.

Example: 

```
import boto3

session = boto3.Session(profile_name="dev")
ec2_client = session.client("ec2")
```

#### EC2 Reservation (Important Concept)

When calling `describe_instances()`, AWS does not return a flat list of instances. Instead, responses are grouped into Reservations.
Originally, AWS supported reserving instance capacity in batches. One reservation might include multiple instances.

A reservation is just a wrapper or group that contains one or more EC2 instances, It’s how AWS organizes the data internally before giving it back to you, Even if you only have one instance, AWS will still wrap it in a reservation.

Let’s say you ask AWS: 
"Hey, give me a list of all my EC2 instances!" 
Now, AWS says: 
"Sure! But I’m going to return them grouped in containers called reservations." 
Imagine AWS is giving you oranges (your EC2 instances), but they always pack them in boxes (reservations). So: 
• You have: 
      
- Box 1 →  EC2 #1, EC2 #2
- Box 2 →  EC2 #3  
- Box 3 → (empty)

If you want to reach all oranges, you have to: 
1. Open each box (loop through reservations) 
2. Take out the oranges (loop through instances inside each reservation).

```
response = ec2_client.describe_instances()

instances = [
    instance
    for reservation in response["Reservations"]
    for instance in reservation["Instances"]
]

print(instances)
```

It seems like that:
   ```
   {
  "Reservations": [
    {
      "ReservationId": "...",
      "Instances": [
        { "InstanceId": "i-001" },
        { "InstanceId": "i-002" }
      ]
    }
  ]
}
```

got it...

#### Full Example

```
import boto3

# Create session
session = boto3.Session(profile_name="default")

# Create client & resource
ec2_client = session.client("ec2")
ec2 = session.resource("ec2")

# Launch an instance
instance = ec2.create_instances(
    ImageId="ami-0c12345",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
)[0]

print("Launching:", instance.id)

# Wait for running
instance.wait_until_running()

# Refresh state
instance.reload()
print("State:", instance.state)

# List running instances using paginator
paginator = ec2_client.get_paginator("describe_instances")

for page in paginator.paginate(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
):
    for reservation in page["Reservations"]:
        for inst in reservation["Instances"]:
            print("Running:", inst["InstanceId"])
```
[section:end]

The AWS SDK for Python (Boto3) is a powerful, flexible framework for managing cloud operations. Its dual API model (clients + resources), together with paginators, waiters, and sessions, makes it suitable for everything from simple automation scripts to large-scale cloud applications.

