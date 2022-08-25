# coding: utf-8
from Mod_Ctr import *
#Import the Controller and Module class definition and the list of modules
from flask import Flask, jsonify, abort, make_response, request, url_for
import random

#Experiments functions
#Average of output when input is a normal distribution [1, 10]
def average(controller):
    n = 100000
    total = 0
    for i in range (n):
        x = random.randint(1,10)
        total += controller.execute(x)
    return total / n

#Absolute difference between the output and a value for a fixed input
def value(controller):
    #This value can be changed or input as a parameter
    input = 5
    val = 35
    return abs(val - controller.execute(input))

#Experiment list
exp_id_list = {'average': average, 'value': value}


#Flask API
app = Flask(__name__)

@app.route('/controller', methods=["POST"])
def receive_controller():
    #Recive the controller for testing and the json with the exp
    rx = request.json
    print(rx)
    controller_json = rx['controller']
    experiments = rx['experiments']
    controller = json_to_ctr(controller_json)
    results_dict = {}
    for e in experiments:
        results_dict[e] = exp_id_list[e](controller)
    #Select the experiments, run them and collect the result list
    # Send the result list back to the Exp_Mg
    return jsonify({ 'type': 'exp_rep', 'results': results_dict }), 201

if __name__ == "__main__":
    #Run the FLASK API
    app.run(debug = True, host = '0.0.0.0', port = '6002')  
