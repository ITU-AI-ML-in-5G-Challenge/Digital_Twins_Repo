# Controller Deployment
Tosca parsing for the deployment of a rest API given the cid of a controller. The orchestrator used is xOpera. The API will answer HTTP GET petitions with a float input with a json that contains the return output given by the deployed controller.

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
The orchestration tool is available on PyPI as a package named [opera]. 
Apart from the latest [PyPI production] version, you can also find the latest opera [PyPI development] version, which 
includes pre-releases so that you will be able to test the latest features before they are officially released.

The simplest way to test `opera` is to install it into Python virtual environment:

```console
$ mkdir ~/opera && cd ~/opera
$ python3 -m venv .venv && . .venv/bin/activate
(.venv) $ pip install opera
```

## Controller Deployment
In `inputs.yaml` introduce the url for getting the json description of the controller from the marketplace.

* Deploy the service by runing:
```console
(.venv) $ opera deploy service.yaml -i inputs.yaml
```
Now the API is deployed and will reply to HTTP GET petitions. You can check it in your browser with the url http://localhost:5000/controller/1.0 . Instead of 1.0 any other float input can be introduced.

* Undeploy the service:
```console
(.venv) $ opera undeploy
```