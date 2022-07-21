"""
Given a JSON object with nested objects, write a function flatten_json that flattens all the objects to a single key-value dictionary. Do not use the library that actually performs this function.

Example:

Input:

import json
json_str = json.dumps({'a':{'b':'c', 'd':'e'}})
Output:

def flatten_json(json_str) -> json.dumps({'a_b':'c', 'a_d':'e'})
Note: Input and output are in string format : use json.dumps() to convert python dictionary to string.

# SAMPLE TEST

def test_flatten_json_double_nested():
    import json
    input_json = json.dumps({
        'A':'C',
        'B':{'D':'E'},
        'F':{
            'G':'H'
        }
    })


    true_output = json.dumps({
        'A':'C', 'B_D':'E','F_G':'H'
    })


    test_output = flatten_json(input_json)
    assert test_output == true_output
    
    
    def test_flatten_json_triple_nested():
    import json
    input_json = json.dumps({
        'A':'C',
        'B':{'D':'E'},
        'F':{
            'G':{'H':'I'}
        }
    })


    true_output = json.dumps({
        'A':'C', 'B_D':'E','F_G_H':'I'
    })


    test_output = flatten_json(input_json)
    assert test_output == true_output
    
    
    def test_flatten_json_quadra_nested():
    import json
    input_json = json.dumps({
        'A':'C',
        'B':{'D':'E'},
        'F':{
            'G':{'H':{'I':'J'}}
        }
    })


    true_output = json.dumps({
        'A':'C', 'B_D':'E','F_G_H_I':'J'
    })


    test_output = flatten_json(input_json)
    assert test_output == true_output

"""
import json
def flatten_json(json_str):
    json_dict = json.loads(json_str)
    result_obj = {}

    def flatten_recurive(keys,jobj):
        if type(jobj) is dict:
            for key in jobj.keys():
                flatten_recurive(keys+[key],jobj[key])
        else:
            # if it is not dictionary type create KEYS
            key_str = '_'.join(keys)
            result_obj[key_str] = jobj
    
    flatten_recurive([],json_dict)
    return json.dumps(result_obj)



