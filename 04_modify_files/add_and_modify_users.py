import json

with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)

new_user = {
    "name": "Andrew",
    "age": 34,
    "student": False
}
users.append(new_user)

for user in users:
    if user["student"]:
        user["age"] += 1
        
    if user["name"] == "Andrew":
        user["city"] = "Budapest"
        user.pop("student")

with open("users.json", "w", encoding="utf-8") as file:
    json.dump(users, file, indent=4)

with open("users.json", "r", encoding="utf-8") as file:
    print(json.load(file))