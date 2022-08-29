# coding: utf-8
from Mod_Ctr import *
from flask import Flask, jsonify, abort, make_response, request, url_for
import json

# Opening JSON file
f = open('ctr.json')

ctr_json = json.load(f)
# ctr_json = {'type': 'controller', 'id':0, 'modules':['mul','sub'], 'parameters':[5, 3]}
ctr = json_to_ctr(ctr_json)
ctr_dict = ctr.get_dict()
print(ctr_dict)

#Flask API
app = Flask(__name__)

@app.route('/controller/<float:x>', methods=["GET"])
def receive_query(x):

    return jsonify({'controller': ctr_dict, 'input': x, 'output': ctr.execute(x)}), 201

if __name__ == "__main__":
    #Run the FLASK API
    app.run(debug = True, host = '0.0.0.0', port = '5000')  
