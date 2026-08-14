user = {
    "name": "Adam",
    "age": -5
}

try:
    if user["age"] < 0:
        raise ValueError("Invalid age!")
except ValueError as error:
    print(error)
else:
    print("Age is valid!")