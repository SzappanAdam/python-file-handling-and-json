import json

with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)

user["age"] = 22
user["city"] = "Budapest"

if "student" in user:
    del user["student"]

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)

with open("user.json", "r", encoding="utf-8") as file:
    print(json.load(file))