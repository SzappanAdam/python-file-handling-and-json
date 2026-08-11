import json


try:
    with open("user.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print("JSON successfully loaded!")

except json.JSONDecodeError:
    print("Invalid JSON!")