# Team Digital Twins: Decentralized Controller Evolution Architecture Including an Integrated Marketplace
This repository contains the code, report, slides and demo video of Team Digital Twins' submission to the 2022 AI/ML in 5G Challenge. We present a Proof of Concept (PoC) of the decentralized controller evolution architecture for Autonomous Networks (AN) using a distributed Marketplace.

# Table of Contents
1. [Introduction](#introduction)
2. [Demo](#demo)
3. [Installation and Reproduction](#quick-start)
4. [Troubleshooting](#troubleshooting)

## Introduction

## Demo

You can find a video demo of this project [here](https://drive.google.com/file/d/1RcLGaupZk4i-S_hT8INUxz5pNFhPREmd/view?usp=sharing).


## Installation and Reproduction

### Pre-requisites
* Docker Engine and Docker Compose: https://www.docker.com/get-started/

### Quick-start

To start the network run the following command in your terminal from the working directory:
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

> **Note** Once deployed, you can gain access the uploaded artifacts on your browser by accessing the IPFS HTTP API of each node. 
> 
> For instance, you could connect to the HTTP API for the Evolution Controller node in your browser with the url http://0.0.0.0:8080/ipfs/ + **< your-file-cid >**
> The different port mappings for each node are listed below: 
> * Evol_Ctr: 8080
> * Exp_Mg: 8091
> * DT: 8092
> * Cur_Ctr: 8093




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
