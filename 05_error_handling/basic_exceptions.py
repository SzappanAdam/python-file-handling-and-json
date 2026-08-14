# FileNotFoundError
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found!")

print("Program finished.")

# KeyError

user = {
    "name": "Adam",
    "age": 21
}

try:
    print(user["city"])
except KeyError:
    print("City key does not exist!")

# ValueError
try:
    age = int("twenty")
except ValueError:
    print("Invalid age!")

print("Program finished.")

# TypeError

try:
    age = "21"
    result = age + 5
except TypeError:
    print("Wrong type!")

print("Program finished.")

# JSONDecodeError

import json

try:
    with open("user.json", "r", encoding="utf-8") as file:
        user = json.load(file)

    print(user["name"])

except FileNotFoundError:
    print("File not found!")

except json.JSONDecodeError:
    print("Invalid JSON!")