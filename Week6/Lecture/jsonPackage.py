import json

data = {
    'name':'joe',
    'age':21,
    "student":True
}

file = open("simple.json",'w')
jsonString = json.dumps(data)
print(jsonString)