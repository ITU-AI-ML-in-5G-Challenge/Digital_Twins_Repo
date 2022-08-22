# Docker Network for FGAN Digital Twins

## Pre-requisites
* Docker Engine and Docker Compose: https://www.docker.com/get-started/

## Quick-start
Begin by enabling swarm mode by running the following command:
```sh
docker swarm init
```
Then, to start the network run the following command in your terminal from the working directory:
```sh
docker compose up -d
```
> **Note** The -d parameter in the previous command runs each container in the background. To display the logs of the entire network you can run:
> ```sh
> docker compose logs -f 
> ```
> or for a specific container:
> ```sh
> docker compose logs -f <my-container>
> ```

To stop the network and remove the containers run: 

```sh
docker compose down
```

## Troubleshooting
The following is a list of useful commands to run for troubleshooting or solving issues while building the project:
* Clear docker's build cache:
```sh
docker builder prune -a
```
* Remove the images of each container in the network:
```sh
bash ./clean.sh
```
* List all containers (running or not):
```sh
docker ps -a
```
* Remove all stopped containers:
```sh
docker container prune 
```
