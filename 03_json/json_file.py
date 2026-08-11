import json

user = {
    "name": "Adam",
    "age": 21,
    "student": True,
    "languages": ["Python", "SQL"]
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)

with open("user.json", "r", encoding="utf-8") as file:
    loaded_user = json.load(file)

print(loaded_user)
print(type(loaded_user))

print(loaded_user["name"])
print(loaded_user["languages"])
