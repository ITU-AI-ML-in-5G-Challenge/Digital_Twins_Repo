# coding: utf-8
import json
import itertools
#Import the Controller and Module class definition and the list of modules
from Mod_Ctr import *
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

experiment_results = []
controller_list = []

if __name__ == "__main__":
    #The assumption is that the Evol_Ctr already has the list of Modules
    module_keys_list = list(module_dict.keys())
    #Let's assume only two possiblities for the tunning parameters
    param_list = [2, 10]
    #In this proof of concept just use combinations of 2 modules
    l_mod = 2 # The number of modules per controller
  
    n_mod = len(module_keys_list) #The number of modules (funtions) avaliable
    permutations_modules = list(itertools.product(list(range(n_mod)), repeat = l_mod))
    n_perm_mod = len(permutations_modules)

    n_param = len(param_list) #The number of possibilities for the parameter tunning
    permutations_param = list(itertools.product(list(range(n_param)), repeat = l_mod ))
    n_perm_param = len(permutations_param)

    counter = 1
    # The loop for testing all permutations
    for n in range(n_perm_mod):
        positions = permutations_modules[n]
        modules = [init_Module(module_keys_list[p]) for p in positions]
        #Fo each combination of modules try all the possible parameters combinations
        for k in range(n_perm_param):
            positions = permutations_param[k]
            parameters = [param_list[p] for p in positions]
            controller = Controller(modules, parameters, counter)
            counter += 1
            #Now get the json for the controller and send to the Market Place, wait and collec the results
            cdict = controller.get_dict()
            json_string = json.dumps(cdict)
            data = {'file' : json_string}
            print(data)

            #Set a retry strategy in case the marketplace is not yet up
            retry_strategy = Retry(total= 10, backoff_factor = 1)
            print(retry_strategy)
            adapter = HTTPAdapter(max_retries = retry_strategy)
            http = requests.Session()
            http.mount("https://", adapter)
            http.mount("http://", adapter)

            res = http.post('http://172.16.239.13:3000/upload', json = data)
            returned_data = res.json()
            print(returned_data)




