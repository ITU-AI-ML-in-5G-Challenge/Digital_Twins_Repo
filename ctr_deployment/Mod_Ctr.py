#Definition of Modules functions and Module class
import math

def f_mul(x, param):
    return x * param

def f_sum(x, param):
    return x + param

def f_sub(x, param):
    return x - param

def f_pow(x, param):
    return math.pow(x, param)


class Module:
    def __init__(self, f, id, rep, param):
        self.function = f
        self.id = id 
        self.param = param
        self.rep = rep #A string representation of the Module
    def set_param(self, param):
        self.param = param
    def get_param(self):
        return self.param
    def get_id(self):
        return self.id
    def execute (self, x):
        return self.function(x, self.param)

#Dictionary with all the possible modules and the correct arguments for their initialitation
module_dict = {'mul': [f_mul,'mul', '*', 10], 'sum': [f_sum,'sum', '+', 10],
 'sub': [f_sub,'sub', '-', 10] , 'pow': [f_pow,'pow', '^', 2]}

#Funtion for initialize a Module with the key of module_dict
def init_Module(key):
    return Module(*module_dict[key])

#Definition of Controller class
#In this case a Controller is just a nested function made up of the modules
class Controller:
    def __init__(self, modules, params, id):
        self.modules = modules #a list of modules
        self.id = id
        self.params = params #List of parameters to configure the Modules
        for i in range(len(modules)):
            self.modules[i].set_param(self.params[i])
    def execute(self, x):
        result = x
        for m in self.modules:
            result = m.execute(result)
        return result
    def get_param(self):
        param = []
        for m in self.modules:
            param.append(m.get_param())
        return param
    def get_rep(self):
        # Get the representantion of the whole chain of modules
        n = len(self.modules)
        rep = '(' * n + 'x'
        for m in self.modules:
            rep += m.rep + str(m.get_param()) + ')'
        return rep
    def get_dict(self):
        #Get a dictionary that describes the Controller attributes
        dictionary = {}
        dictionary["type"] = "controller"
        dictionary["id"] = self.id
        modules_id = []
        for m in self.modules:
            modules_id.append(m.get_id())
        dictionary["modules"] = modules_id
        dictionary["parameters"] = self.get_param()
        dictionary["representation"] = self.get_rep()
        return dictionary

#Function to create controller from its dictionary representation
def json_to_ctr(dictionary):
    id = dictionary["id"]
    modules_id = dictionary["modules"]
    parameters = dictionary["parameters"]
    modules = []
    for mid in modules_id:
        modules.append(init_Module(mid))
    return Controller(modules, parameters, id)