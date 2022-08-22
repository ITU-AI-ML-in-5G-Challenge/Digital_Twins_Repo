# Controller Deployment
Tosca parsing for the deployment of a REST service given the cid of a controller. The orchestrator used is xOpera. The service will answer HTTP GET requests that contains a float input with a json that contains the output returned by the deployed controller.

## Prerequisites
> **Note** Prerequisites and the Installation and Quickstart are copied from the xOpera repository: https://github.com/xlab-si/xopera-opera
> Run the commands inside the /ctr_deployment directory

`opera` requires Python 3 and a virtual environment. 
In a typical modern Linux environment, we should already be set. 
In Ubuntu, however, we might need to run the following commands:

```console
$ sudo apt update
$ sudo apt install -y python3-venv python3-wheel python-wheel-common
```
## Installation and Quickstart
The simplest way to test `opera` is to install it into Python virtual environment:

```console
$ mkdir ~/opera && cd ~/opera
$ python3 -m venv .venv && . .venv/bin/activate
(.venv) $ pip install opera
```

## Controller Deployment
In `inputs.yaml` introduce the url for getting the json description of the controller from the marketplace. **ALSO CHANGE THE VARIABLE PATH** with the current absolute path (the output when running `pwd` inside `/ctr_deployment`).

* Deploy the service by running:
```console
(.venv) $ opera deploy service.yaml -i inputs.yaml
```
Now the service is deployed and will reply to HTTP GET requests. You can check it in your browser with the url http://localhost:5000/controller/1.0 . Instead of 1.0, any other float input can be introduced.

* Undeploy the service:
```console
(.venv) $ opera undeploy
```