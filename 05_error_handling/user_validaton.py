import json

try:
    with open("user.json", "r", encoding="utf-8") as file:
        user = json.load(file)

    name = user["name"]
    age = user["age"]
    student = user["student"]

    if age < 0:
        raise ValueError("Age cannot be negative!")

except FileNotFoundError:
    print("File not found!")

except json.JSONDecodeError:
    print("Not JSON!")

except KeyError:
    print("Key does not exist!")

except ValueError as error:
    print(error)

else:
    print("User data is valid!")

finally:
    print("Validation finished.")