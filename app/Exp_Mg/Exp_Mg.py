# coding: utf-8
import json
#Import the Controller and Module class definition and the list of modules
from Mod_Ctr import *
from flask import Flask, jsonify, abort, make_response, request, url_for
import requests

# The list of experiments
exp_id_list = ['average', 'value'] #If DT updates the list of exp it must be notified

#Flask API
app = Flask(__name__)

@app.route('/controller', methods=["POST"])
def receive_controller():
    rx = request.json #Get the json for the controller sent by the marketplace
    exp_list = [exp_id_list[0], exp_id_list[1]] #The list of experiments to be run
    data = {'controller': rx, 'experiments': exp_list, 'param':[]} # Send to the DT the controller 
    #and the list of experiments 
    results = requests.post('http://172.16.239.31:6002/controller', json = data)
    # With the DT results send the exp_rep back to the marketplace with the id of the ctr and the expriment 
    results = results.json()
    results['id'] = rx['id'] #Add the id of the controller
    json_string = json.dumps(results)
    data = {'file' : json_string}
    print(data)
    # Upload the exp_rep to the Market Place
    res = requests.post('http://172.16.239.23:3000/upload', json = data)
    print(res)
    return rx, 201

if __name__ == "__main__":
    #Run the FLASK API
    app.run(debug = True, host = '0.0.0.0', port = '6001') 