import json


def load_users(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(filename, users):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def add_user(users, name, age, student=False):
    new_user = {
        "name": name,
        "age": age,
        "student": student
    }
    users.append(new_user)


def update_user(users, name, new_age):
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            return True

    return False


def delete_user(users, name):
    for user in users:
        if user["name"] == name:
            users.remove(user)
            return True

    return False


def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None

users = load_users("users.json")

add_user(users, "Emma", 24, True)

updated = update_user(users, "Lisa", 22)

if updated:
    print("User updated!")
else:
    print("User not found!")

adam = find_user(users, "Adam")
print(adam)

delete_user(users, "Andrew")

save_users("users.json", users)