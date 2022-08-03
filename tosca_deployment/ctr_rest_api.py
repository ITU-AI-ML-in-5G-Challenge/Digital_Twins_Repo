# coding: utf-8
from Mod_Ctr import *
from flask import Flask, jsonify, abort, make_response, request, url_for
import sys

ctr_json = {'type': 'controller', 'id':0, 'modules':['mul','sub']}
ctr = json_to_ctr(ctr_json)
ctr_dict = ctr.get_dict()
print(ctr_dict)

#Flask API
app = Flask(__name__)

@app.route('/controller/<float:x>', methods=["GET"])
def receive_query(x):
    #Recive the controller for testing and the json with the exp

    return jsonify({'controller': ctr_dict, 'input': x, 'output': ctr.execute(x)}), 201

if __name__ == "__main__":
    #Run the FLASK API
    app.run(debug = True, host = '0.0.0.0', port = '5000')  
