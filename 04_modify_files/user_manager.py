import json

with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)

new_user = {
    "name": "Emma",
    "age": 24,
    "student": True,
    "languages": ["Python"]
}
users.append(new_user)

student_count = 0
for user in users:
    current_name = user["name"]
    student = user["student"]
    if current_name == "Adam":
        user["age"] += 1
    if current_name == "Lisa":
        user["city"] = "Budapest"
    if student:
        user["active"] = True
        student_count += 1
    if current_name == "Andrew":
        user.pop("student", None)


with open("users.json", "w", encoding="utf-8") as file:
    json.dump(users, file, indent=4)
    
print(f"Active students: {student_count}")

with open("users.json", "r", encoding="utf-8") as file:
    print(json.load(file))
