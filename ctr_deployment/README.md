# Controller Deployment
Tosca parsing for the deployment of a rest API given the cid of a controller. The orchestrator used is xOpera

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
In inputs.yaml change path and path_ctr_json. Select the json description of the controller url
opera deploy service.yaml -i inputs.yaml
opera undeploy