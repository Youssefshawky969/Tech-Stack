## What is a registry?

Now that you know what a container image is and how it works, you might wonder - where do you store these images?

Well, you can store your container images on your computer system,

but what if you want to share them with your friends or use them on another machine? That's where the image registry comes in.

An image registry is a centralized location for storing and sharing your container images. 

It can be either public or private. Docker Hub is a public registry that anyone can use and is the default registry.

While Docker Hub is a popular option, there are many other available container registries available today, including Amazon Elastic Container Registry (ECR), Azure Container Registry (ACR), and Google Container Registry (GCR). 

You can even run your private registry on your local system or inside your organization. For example, Harbor, JFrog Artifactory, GitLab Container registry etc.

## Registry vs. repository

While you're working with registries, you might hear the terms registry and repository as if they're interchangeable.

Even though they're related, they're not quite the same thing.

A registry is a centralized location that stores and manages container images, whereas a repository is a collection of related container images within a registry. 

Think of it as a folder where you organize your images based on projects.

Each repository contains one or more container images.

The following diagram shows the relationship between a registry, repositories, and images.

<img width="878" height="835" alt="image" src="https://github.com/user-attachments/assets/bf881b8f-a63a-4156-a4a0-b7873433d0e5" />

### learn how to build and push a Docker image to the Docker Hub repository.

1- If you haven't created one yet, head over to the Docker Hub page to sign up for a new Docker account. Be sure to finish the verification steps sent to your email.

<img width="871" height="553" alt="image" src="https://github.com/user-attachments/assets/300412c7-1a1c-49ab-87ac-fc54b5f8318d" />


You can use your Google or GitHub account to authenticate.

#### Create your first repository

1- Sign in to Docker Hub.
2- Select the Create repository button in the top-right corner.
3- Select your namespace (most likely your username) and enter docker-quickstart as the repository name.


<img width="1999" height="960" alt="image" src="https://github.com/user-attachments/assets/498ce62f-f87b-43df-837f-8b1a5d5fbdd4" />

4- Set the visibility to Public.
5- Select the Create button to create the repository.

That's it. You've successfully created your first repository. 🎉

#### Sign in with Docker Desktop

1- Download and install Docker Desktop, if not already installed.
2- In the Docker Desktop GUI, select the Sign in button in the top-right corner
3- Navigate into the newly created directory.
4- Run the following command to build a Docker image, swapping out `YOUR_DOCKER_USERNAME` with your username.

```bash
docker build -t YOUR_DOCKER_USERNAME/docker-quickstart .
```

> [!NOTE]
> Make sure you include the dot (`.`) at the end of the docker build command. This tells Docker where to find the Dockerfile.

5- Run the following command to list the newly created Docker image:
```bash
docker images
```

You will see output like the following:

```bash
REPOSITORY                                 TAG       IMAGE ID       CREATED         SIZE
YOUR_DOCKER_USERNAME/docker-quickstart   latest    476de364f70e   2 minutes ago   170MB
```

6- Start a container to test the image by running the following command (swap out the username with your own username):
```bash
docker run -d -p 8080:8080 YOUR_DOCKER_USERNAME/docker-quickstart
```

You can verify if the container is working by visiting http://localhost:8080 with your browser.


7- Use the docker tag command to tag the Docker image.
  - Docker tags allow you to label and version your images.

```bash
docker tag <YOUR_DOCKER_USERNAME>/docker-quickstart <YOUR_DOCKER_USERNAME>/docker-quickstart:1.0
```

8- Finally, it's time to push the newly built image to your Docker Hub repository by using the `docker push` command:
```bash
docker push <YOUR_DOCKER_USERNAME>/docker-quickstart:1.0
```



