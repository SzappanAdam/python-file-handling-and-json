import json


# Python dict -> JSON string

user = {
    "name": "Adam",
    "age": 21,
    "student": True
}

json_data = json.dumps(user)

print(json_data)
print(type(json_data))


# Python list -> JSON string

users = [
    {"name": "Adam", "age": 21},
    {"name": "Anna", "age": 22},
    {"name": "Peter", "age": 20}
]

json_data = json.dumps(users)

print(json_data)
print(type(json_data))


# JSON string -> Python dict

json_data = '{"name": "Adam", "age": 21, "student": true}'

user = json.loads(json_data)

print(user)
print(type(user))

print(user["name"])
print(user["age"])
print(user["student"])