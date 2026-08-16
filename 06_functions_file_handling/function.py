def greet(name):
    print(f"Hello {name}!")

greet("Adam")
greet("Lisa")
greet("Andrew")

##

def calculate_age(birth_year):
    return 2026-birth_year

age = calculate_age(2005)
print(age)

##

def is_adult(age):
    return age >= 18

print(is_adult(21))
print(is_adult(16))

##

user = {
    "name": "Adam",
    "age": 21
}

def get_user_name(user):
    return user["name"]

name = get_user_name(user)
print(name)

##

def create_user(name, age, student=False):
    return {
        "name": name,
        "age": age,
        "student": student
    }

print(create_user("Adam", 21))
print(create_user("Lisa", 20, True))