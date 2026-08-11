import json


users = [
    {
        "name": "Adam",
        "age": 21,
        "student": True,
        "languages": ["Python", "SQL"]
    },
    {
        "name": "Lisa",
        "age": 20,
        "student": True,
        "languages": ["Java", "JavaScript"]
    },
    {
        "name": "Andrew",
        "age": 34,
        "student": False,
        "languages": ["Ruby"]
    }
]


# Python list[dict] -> JSON string
json_data = json.dumps(users, indent=4)

print(json_data)


# JSON string -> Python list[dict]
loaded_users = json.loads(json_data)

print(loaded_users[0]["name"])
print(loaded_users[1]["languages"])
print(loaded_users[2]["student"])


# Iterate through nested data
for user in users:
    result = ", ".join(user["languages"])
    print(user["name"], "->", result)