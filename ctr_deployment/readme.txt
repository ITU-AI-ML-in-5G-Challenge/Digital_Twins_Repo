sudo apt update
sudo apt install -y python3-venv python3-wheel python-wheel-common

python3 -m venv .venv && . .venv/bin/activate
pip install --upgrade pip
pip install opera

In inputs.yaml change path and path_ctr_json. Select the json description of the controller url

opera deploy service.yaml -i inputs.yaml
opera undeploy