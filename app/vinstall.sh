#!/bin/sh
#This program installs the virtual enviroment and the python packages needed
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install python-math
pip install requests_html
