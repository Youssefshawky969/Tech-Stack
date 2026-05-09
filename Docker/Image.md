## What is an image?

Seeing as a container is an isolated process, where does it get its files and configuration? How do you share those environments?

That's where container images come in. 

A container image is a standardized package that includes all of the files, binaries, libraries, and configurations to run a container.

For a PostgreSQL image, that image will package the database binaries, config files, and other dependencies.

For a Python web app, it'll include the Python runtime, your app code, and all of its dependencies.

There are two important principles of images:

1- Images are immutable.
  - Once an image is created, it can't be modified.
  - You can only make a new image or add changes on top of it.

2- Container images are composed of layers.
  - Each layer represents a set of file system changes that add, remove, or modify files.


These two principles let you to extend or add to existing images. 

For example, if you are building a Python app, you can start from the Python image and add additional layers to install your app's dependencies and add your code.

This lets you focus on your app, rather than Python itself.

### Finding images

Docker Hub is the default global marketplace for storing and distributing images.

 It has over 100,000 images created by developers that you can run locally.

 You can search for Docker Hub images and run them directly from Docker Desktop.

 #### Search for and download an image
 
Follow the instructions to search and pull a Docker image using CLI to view its layers.

1- Open a terminal and search for images using the `docker search` command:

```bash
docker search docker/welcome-to-docker
```

You will see output like the following:

```bash
NAME                       DESCRIPTION                                     STARS     OFFICIAL
docker/welcome-to-docker   Docker image for new users getting started w…   20
```

This output shows you information about relevant images available on Docker Hub.

2- Pull the image using the `docker pull` command.

```bash
docker pull docker/welcome-to-docker
```

You will see output like the following:

```bash
Using default tag: latest
latest: Pulling from docker/welcome-to-docker
579b34f0a95b: Download complete
d11a451e6399: Download complete
1c2214f9937c: Download complete
b42a2f288f4d: Download complete
54b19e12c655: Download complete
1fb28e078240: Download complete
94be7e780731: Download complete
89578ce72c35: Download complete
Digest: sha256:eedaff45e3c78538087bdd9dc7afafac7e110061bbdd836af4104b10f10ab693
Status: Downloaded newer image for docker/welcome-to-docker:latest
docker.io/docker/welcome-to-docker:latest
```

Each of line represents a different downloaded layer of the image. Remember that each layer is a set of filesystem changes and provides functionality of the image.

#### Learn about the image

1- List your downloaded images using the `docker image ls` command:

```bash
docker image ls
```
You will see output like the following:

```bash
REPOSITORY                 TAG       IMAGE ID       CREATED        SIZE
docker/welcome-to-docker   latest    eedaff45e3c7   4 months ago   29.7MB
```

The command shows a list of Docker images currently available on your system. The `docker/welcome-to-docker` has a total size of approximately 29.7MB.

>[!NOTE]
>
>The image size represented here reflects the uncompressed size of the image, not the download size of the layers.


2- List the image's layers using the `docker image history` command:

```bash
docker image history docker/welcome-to-docker
```

You will see output like the following:

```bash
IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
648f93a1ba7d   4 months ago   COPY /app/build /usr/share/nginx/html # buil…   1.6MB     buildkit.dockerfile.v0
<missing>      5 months ago   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>      5 months ago   /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
<missing>      5 months ago   /bin/sh -c #(nop)  EXPOSE 80                    0B
<missing>      5 months ago   /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B
<missing>      5 months ago   /bin/sh -c #(nop) COPY file:9e3b2b63db9f8fc7…   4.62kB
<missing>      5 months ago   /bin/sh -c #(nop) COPY file:57846632accc8975…   3.02kB
<missing>      5 months ago   /bin/sh -c #(nop) COPY file:3b1b9915b7dd898a…   298B
<missing>      5 months ago   /bin/sh -c #(nop) COPY file:caec368f5a54f70a…   2.12kB
<missing>      5 months ago   /bin/sh -c #(nop) COPY file:01e75c6dd0ce317d…   1.62kB
<missing>      5 months ago   /bin/sh -c set -x     && addgroup -g 101 -S …   9.7MB
<missing>      5 months ago   /bin/sh -c #(nop)  ENV PKG_RELEASE=1            0B
<missing>      5 months ago   /bin/sh -c #(nop)  ENV NGINX_VERSION=1.25.3     0B
<missing>      5 months ago   /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
<missing>      5 months ago   /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      5 months ago   /bin/sh -c #(nop) ADD file:ff3112828967e8004…   7.66MB
```

This output shows you all of the layers, their sizes, and the command used to create the layer.

>[!NOTE]
> If you add the `--no-trunc` flag to the command, you will see the full command.
> Note that, since the output is in a table-like format, longer commands will cause the output to be very difficult to navigate.


## Writing a Dockerfile

A Dockerfile is a text-based document that's used to create a container image. It provides instructions to the image builder on the commands to run, files to copy, startup command, and more.

As an example, the following Dockerfile would produce a ready-to-run Python application:

```dockerfile
FROM python:3.13
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src ./src
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### Common instructions

Some of the most common instructions in a Dockerfile include:

- `FROM <image>` - this specifies the base image that the build will extend.
- `WORKDIR <path>` - this instruction specifies the "working directory" or the path in the image where files will be copied and commands will be executed.
- `COPY <host-path>` <image-path> - this instruction tells the builder to copy files from the host and put them into the container image.
- `RUN <command>` - this instruction tells the builder to run the specified command.
- `ENV <name> <value>` - this instruction sets an environment variable that a running container will use.
- `EXPOSE <port-number>` - this instruction sets configuration on the image that indicates a port the image would like to expose.
- `USER <user-or-uid>` - this instruction sets the default user for all subsequent instructions.
- `CMD ["<command>", "<arg1>"]` - this instruction sets the default command a container using this image will run.

## Build, tag, and publish an image

### Building images

Most often, images are built using a Dockerfile. The most basic `docker build` command might look like the following:
```bash
docker build .
```

When you run a build, the builder pulls the base image, if needed, and then runs the instructions specified in the Dockerfile.

With the previous command, the image will have no name, but the output will provide the ID of the image. As an example, the previous command might produce the following output:

```bash
$ docker build .
[+] Building 3.5s (11/11) FINISHED                                              docker:desktop-linux
 => [internal] load build definition from Dockerfile                                            0.0s
 => => transferring dockerfile: 308B                                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.12                                  0.0s
 => [internal] load .dockerignore                                                               0.0s
 => => transferring context: 2B                                                                 0.0s
 => [1/6] FROM docker.io/library/python:3.12                                                    0.0s
 => [internal] load build context                                                               0.0s
 => => transferring context: 123B                                                               0.0s
 => [2/6] WORKDIR /usr/local/app                                                                0.0s
 => [3/6] RUN useradd app                                                                       0.1s
 => [4/6] COPY ./requirements.txt ./requirements.txt                                            0.0s
 => [5/6] RUN pip install --no-cache-dir --upgrade -r requirements.txt                          3.2s
 => [6/6] COPY ./app ./app                                                                      0.0s
 => exporting to image                                                                          0.1s
 => => exporting layers                                                                         0.1s
 => => writing image sha256:9924dfd9350407b3df01d1a0e1033b1e543523ce7d5d5e2c83a724480ebe8f00    0.0s
```

With the previous output, you could start a container by using the referenced image:

```bash
docker run sha256:9924dfd9350407b3df01d1a0e1033b1e543523ce7d5d5e2c83a724480ebe8f00
```

That name certainly isn't memorable, which is where tagging becomes useful.

### Tagging images

Tagging images is the method to provide an image with a memorable name. However, there is a structure to the name of an image. A full image name has the following structure:

```
[HOST[:PORT_NUMBER]/]PATH[:TAG]
```

- `HOST`: The optional registry hostname where the image is located. If no host is specified, Docker's public registry at `docker.io` is used by default.
- `PORT_NUMBER`: The registry port number if a hostname is provided
- `PATH`: The path of the image, consisting of slash-separated components. For Docker Hub, the format follows `[NAMESPACE/]REPOSITORY`, where namespace is either a user's or organization's name. If no namespace is specified, `library` is used, which is the namespace for Docker Official Images.

- `TAG`: A custom, human-readable identifier that's typically used to identify different versions or variants of an image. If no tag is specified, `latest` is used by default.

Some examples of image names include:
- `nginx`, equivalent to `docker.io/library/nginx:latest:` this pulls an image from the `docker.io` registry, the `library` namespace, the `nginx` image repository, and the `latest` tag.
- `docker/welcome-to-docker`, equivalent to `docker.io/docker/welcome-to-docker:latest:` this pulls an image from the `docker.io` registry, the `docker` namespace, the `welcome-to-docker` image repository, and the `latest` tag
- `ghcr.io/dockersamples/example-voting-app-vote:pr-311:` this pulls an image from the GitHub Container Registry, the `dockersamples` namespace, the `example-voting-app-vote` image repository, and the `pr-311` tag

To tag an image during a build, add the `-t` or `--tag` flag:
```bash
docker build -t my-username/my-image .
```

If you've already built an image, you can add another tag to the image by using the `docker image tag` command:

```bash
docker image tag my-username/my-image another-username/another-image:v1
```

### Publishing images

Once you have an image built and tagged, you're ready to push it to a registry. To do so, use the docker push command:

```bash
docker push my-username/my-image
```


