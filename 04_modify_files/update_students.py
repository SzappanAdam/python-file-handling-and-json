import json

with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)

for user in users:
    if user["student"]:
        user["age"] += 1

with open("users.json", "w", encoding="utf-8") as file:
    json.dump(users, file, indent=4)

with open("users.json", "r", encoding="utf-8") as file:
    print(json.load(file))