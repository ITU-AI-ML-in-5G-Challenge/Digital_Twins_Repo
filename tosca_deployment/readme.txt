sudo apt update
sudo apt install -y python3-venv python3-wheel python-wheel-common

python3 -m venv .venv && . .venv/bin/activate
pip install --upgrade pip
pip install opera
opera deploy service.yaml
opera undeploy