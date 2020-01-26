fully copied from https://www.programiz.com/python-programming/json

#  1) python dict is the equivalent of json object 
 
import json
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)  # this becomes a python dict type 
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)
# Output: ['English', 'French']
print(person_dict['languages'])


# 2) read from file

with open ('path/file.json') as f:
	data = json.load(f)

	
#  3) Covert python dictionary to json object

import json
person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)

#  4) writing json to a file

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)

#  5) pretty print json
  
print(json.dumps(person_dict, indent = 4, sort_keys=True))
{
    "languages": "English",
    "name": "Bob",
    "numbers": [
        2,
        1.6,
        null
    ]
}
  
  
  
  
  
  
  
