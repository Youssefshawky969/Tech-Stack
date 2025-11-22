[section:overview]

### Overveiw

Docker is a complete platform designed to build, package, ship, and run applications using lightweight, isolated containers. Containers solve the common challenge of “works on my machine” by providing the same environment everywhere: developer laptop, on-prem servers, cloud platforms, or CI/CD pipelines.

Docker exists because traditional deployments face issues like dependency conflicts, complex installations, configuration mismatch across environments, and slow provisioning (VM-level).

Docker solves this by packing everything the app needs into one unit (container), ensuring consistent behavior across platforms, deploying applications fast with minimal overhead

[section:architecture]

### Architecture

##### Docker Images:
A Docker image is a read-only template that contains OS base layer (Alpine, Ubuntu, Debian…), Application runtime (Python, Node, Java…), Dependencies, Application code, Startup instructions.

Images are immutable and layered, meaning every Dockerfile instruction creates a new cached filesystem layer.

Example image tags:
```
nginx:latest
python:3.11-slim
myapp:1.0.4
```

##### Docker Containers:

A container is a lightweight, isolated instance created from an image. Its characteristics that it is own filesystem, own process space, lightweight (shares host kernel), ephemeral unless connected to persistent storage, and starts in milliseconds.

##### Docker Engine:

The Docker Engine is the core runtime consisting of dockerd (daemon) that manages containers & images, Docker CLI that main interaction tool, REST API that internal communication layer.

##### Docker Registries:

Registries store and distribute images like Docker Hub, Amazon Elastic Container Registry (ECR), GitHub Container Registry (GHCR), and Google Artifact Registry.

Push Example:

```
docker tag myapp:1.0 ghcr.io/user/myapp:1.0
docker push ghcr.io/user/myapp:1.0
```

##### Docker Networks:

Docker networking models like bridge (default) that isolated network for containers, host, and none that disables networking

Example:
```
docker network create mynetwork
docker run --network=mynetwork app1
```

#### Volumes:

Volumes store data outside the container lifecycle ensuring persistence.

Example:
```
docker volume create dbdata
docker run -v dbdata:/var/lib/mysql mysql
```

##### Dockerfile:

A Dockerfile is a declarative file and sequential set of instructions that describes how to build a Docker image. It reads from top to bottom, and each instruction creates a new image layer.

The first instruction MUST ALWAYS be `FROM`, because it defines the base image (starting point).

```
FROM ubuntu:22.04
```
or
```
FROM python:3.11-slim
```

`LABEL` or `MAINTAINER` for metadata its optional used to describe the image, This layer is added early to maintain metadata.

```
LABEL maintainer="yourname@example.com"
LABEL project="Billing System API"
```

`ARG` buil-time variables decalear before its usage

```
ARG VERSION=1.0
```

`ENV` enviroment variable (Runtime)

```
ENV APP_ENV=production
ENV PYTHONUNBUFFERED=1
```

`WORKDIR` set working directory and sets the default path inside the container for all subsequent operations.

```
WORKDIR /app
```
If the folder does not exist, Docker creates it.

`COPY` or `ADD` bring files into the image but `COPY` is preferred

```
COPY requirements.txt .
COPY src/ ./src
```

`RUN` install dependencies and executed during build time not runtime.

```
RUN apt-get update && apt-get install -y build-essential
RUN pip install -r requirements.txt
```

But take care! ` Every RUN command makes a new layer and using multiple RUN commands increases image size` 

Best practcies is using Combine commands like this:
```
RUN apt-get update \
 && apt-get install -y curl git \
 && apt-get clean
```

`EXPOSE` document the listen port.
```
EXPOSE 5000
```

`ENTRYPOINT` primary execution command defines the program that will always run.

```
ENTRYPOINT ["python", "app.py"]
```
This is the main executable of the container.

`CMD` default arguments to `ENTRYPOINT`

```
CMD ["--port", "5000"]
```

**Full Example:**
if you try to dockerize python application, you probley do something like that

Dockrize:

```
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```
Build the Image:
```
docker build -t myapp:1.0 .
```
Run the container
```
docker run -d -p 5000:5000 myapp:1.0
```
Then Tag and Push to Registry
```
docker tag myapp:1.0 myrepo/myapp:1.0
docker push myrepo/myapp:1.0
```

After that you can deploy anywhere local machines, AWS, Kubernets

```
docker pull myrepo/myapp:1.0
docker run -d -p 80:5000 myrepo/myapp:1.0
```

