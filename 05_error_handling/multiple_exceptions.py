import json

try:
    with open("user.json", "r", encoding="utf-8") as file:
        user = json.load(file)
    user["age"]
except FileNotFoundError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON!")
except KeyError:
    print("Age key does not exist!")