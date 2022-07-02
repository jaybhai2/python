import collections
from typing import Any, Dict, Optional, Union, List, Tuple
import copy
def deep_update_dict_inplace(source_dict, update_chain)-> dict:
    for key, val in update_chain.items():
        if isinstance(val, collections.abc.Mapping) and val:
            if isinstance(source_dict, list):
                returned = deep_update_dict_inplace(source_dict[key], val)
            else:
                returned = deep_update_dict_inplace(source_dict.get(key, {}), val)
            source_dict[key] = returned
        else:
            source_dict[key] = val
    return source_dict

test_source = {'name':'super', 'path':[{'s3':'bucket1'}, {'s3':'bucket2'}], 'config':{'env':{'beta':'1', 'gamme':'2'}}}
test_update_chain1 = {'path':{0:{'s3':'bucketchanged'}}}
test_update_chain2 = {'config':{'env':{'gamme':'4'}}}

print(deep_update_dict_inplace(test_source,test_update_chain1))
print(deep_update_dict_inplace(test_source,test_update_chain2))



def build_chained_dict_from_list(key_list, end_value) -> dict:
    """
    covert ['a','b',1,'c']
    to
    {a: {b: {1: {c: end_value}}}}
    """
    chained_dict = {}
    current_level = chained_dict   # current level points to chained_dict. => {}
    
    for i, v in enumerate(key_list):
        if v not in current_level:
            if i == len(key_list) - 1:
                current_level[v] = end_value
            else:
                current_level[v] = {}     # {a:{}}
        
        current_level = current_level[v]  # current lent point to a, =>{} 
    return chained_dict
    
print(build_chained_dict_from_list( ['a','b',1,'c'], 'end_value'))
    

def deep_get(input_dict, key_path) :
    """
    getting a nested element from a dictionary using key path-[key1, key2, key3, key4]
    
    """
    inner_element = input_dict
    
    for k in key_path:
        if isinstance(inner_element, (dict, list)):
            inner_element = inner_element[k]
        else:
            return inner_element
    return inner_element
    

print(deep_get(test_source, ['path', 0, 's3']))


def find_path_to_key(d:Dict[str, Any], target_key:str)->List[Tuple[List[any], any]]:
    """
    this does not work with nested list element like 
                'path':[
                    [{'s3':'bucket1'}], 
                    [{'s3':'bucket2'}]
                ]
    """
    
    result = []
    temp_path = []
    
    def find_path(dict_obj, key, i=None):
        
        for k, v in dict_obj.items():
            
            # add key to path
            temp_path.append(k)
            
            if isinstance(v, dict):
                find_path(v, key, i) # continue searching inside of dict
                
            elif isinstance(v, list):
                for i, elem in enumerate(v):
                    
                    temp_path.append(i)
                    
                    if isinstance(elem, dict):
                        find_path(elem, key, i) # continue searching inside of list
                    # if reached here. the last added index is incorrect, remove it
                    
                    temp_path.pop()
                    
            if k == key:
                # add path to result
                result.append((copy.copy(temp_path), v))
            # remove the key added in the first line
            if temp_path != []:
                temp_path.pop()
                
    p = find_path(d, target_key)
    
    return result


test_dict = {'name':'super', 'path':[{'s3':'bucket1'}, {'s3':'bucket2'}], 'config':{'env':{'beta':'1', 'gamme':'2'}}}            
    
find_path_to_key(test_dict, 's3')    
