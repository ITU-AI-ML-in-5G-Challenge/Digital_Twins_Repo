# coding: utf-8
import json
from Mod_Ctr import *
#Import the Controller and Module class definition and the list of modules
from flask import Flask, jsonify, abort, make_response, request, url_for
import json
import requests

exp_id_list = ['average', 'value'] #List of avaliable experiments

#Flask API
app = Flask(__name__)

@app.route('/exp_rep', methods=["POST"])
def receive_controller():
    #Recive the controller from the marketplace
    rx = request.json
    results = rx['results']
    print(rx)
    #For each controller check if the result of the experiments are good enough for 
    #promotion to a protected controller and if so, notify the market place
    if(results['average'] > 500):
        ptr_ctr = {"type": "ptr_ctr", "id": rx["id"], "exp": "max_average"}
        json_string = json.dumps(ptr_ctr)
        data = {'file' : json_string}
        res = requests.post('http://172.16.239.43:3000/upload', json = data)
        print(res.json())
        print('Added Max_Avg')

    if(results['value'] < 20):
        ptr_ctr = {"type": "ptr_ctr", "id": rx["id"], "exp": "value"}
        json_string = json.dumps(ptr_ctr)
        data = {'file' : json_string}
        res = requests.post('http://172.16.239.43:3000/upload', json = data)
        print(res.json())
        print('Added Val')

    return rx, 201

if __name__ == "__main__":
    #Run the FLASK API
    app.run(debug = True, host = '0.0.0.0', port = '6003')   


