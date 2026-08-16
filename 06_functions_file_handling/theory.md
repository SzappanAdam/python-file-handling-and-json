# Day 06 — Python Functions

## 📚 Overview

Functions are one of the most important building blocks of Python programs.

They allow us to:

- organize code into smaller, reusable pieces
- avoid repeating the same code
- make programs easier to read
- make programs easier to test and debug
- separate different responsibilities
- reuse logic with different data

Instead of writing the same instructions multiple times, we can place them inside a function and call the function whenever we need it.

---

# 1. What Is a Function?

A function is a reusable block of code designed to perform a specific task.

A simple function looks like this:

```python
def greet():
    print("Hello!")
```

The function does not run when it is defined.

It runs when we call it:

```python
greet()
```

Output:

```text
Hello!
```

---

# 2. Defining a Function

Functions are created using the ```def``` keyword.

```python
def greet(name):
    print(f"Hello {name}!")
```

The general structure is:

```python
def function_name(parameters):
    # function body
```

### Important parts

- ```def``` — tells Python that we are defining a function
- ```function_name``` — the name of the function
- ```parameters``` — optional values the function can receive
- ```:``` — starts the function body
- indented code — the instructions executed by the function

Example:

```python
def greet(name):
    print(f"Hello {name}!")
```

Calling the function:

```python
greet("Adam")
greet("Lisa")
greet("Andrew")
```

Output:

```text
Hello Adam!
Hello Lisa!
Hello Andrew!
```

---

# 3. Parameters and Arguments

A parameter is the variable defined in the function.

An argument is the actual value passed to the function.

```python
def greet(name):
    print(f"Hello {name}!")
```

Here:

```text
name → parameter
```

When we call:

```python
greet("Adam")
```

```"Adam"``` is the argument.

Example

```python
def calculate_age(birth_year):
    return 2026 - birth_year

age = calculate_age(2005)

print(age)
```

Here:

```text
birth_year → parameter
2005       → argument
```

---

# 4. Return Values

A function can return a value using the ```return``` statement.

```python
def calculate_age(birth_year):
    return 2026 - birth_year
```

The returned value can be stored:

```python
age = calculate_age(2005)

print(age)
```

Output:

```text
21
```

The important difference is that ```return``` gives a value back to the code that called the function.

---

# 5. ```print()``` vs ```return```

```print()``` and ```return``` are not the same thing.

```print()```

Displays something on the screen:

```python
def greet(name):
    print(f"Hello {name}!")
```

The function prints the result, but does not return it.

```return```

Sends a value back to the caller:

```python
def calculate_age(birth_year):
    return 2026 - birth_year
```

Now we can use the result:

```python
age = calculate_age(2005)

print(age)
```

We can also perform another operation:

```python
age = calculate_age(2005)

if age >= 18:
    print("Adult")
```

### Key difference

```text
print()
    ↓
display something

return
    ↓
send a value back
```

---

# 6. Functions Returning Boolean Values

Functions can return ```True``` or ```False```.

This is useful when a function answers a yes/no question.

Example:

```python
def is_adult(age):
    return age >= 18
```

Usage:

```python
print(is_adult(21))
print(is_adult(16))
```

Output:

```text
True
False
```

The expression:

```python
age >= 18
```

already produces a Boolean value, so we can return it directly.

---

# 7. Functions and Dictionaries

Functions can receive dictionaries as parameters.

Example:

```python
user = {
    "name": "Adam",
    "age": 21
}

def get_user_name(user):
    return user["name"]

name = get_user_name(user)

print(name)
```

Output:

```text
Adam
```

The function receives the entire dictionary and accesses the required value.

This is especially useful when working with structured data.

---

# 8. Default Parameters

A function parameter can have a default value.

Example:

```python
def create_user(name, age, student=False):
    return {
        "name": name,
        "age": age,
        "student": student
    }
```

We can call the function without providing ```student```:

```python
print(create_user("Adam", 21))
```

Result:

```python
{
    "name": "Adam",
    "age": 21,
    "student": False
}
```

Or we can provide the value explicitly:

```python
print(create_user("Lisa", 20, True))
```

Result:

```python
{
    "name": "Lisa",
    "age": 20,
    "student": True
}
```

Default parameters make functions more flexible.

---

# 9. Functions Working with Lists

Functions can receive lists as parameters.

Example:

```python
def add_user(users, name, age, student=False):
    user = {
        "name": name,
        "age": age,
        "student": student
    }

    users.append(user)
```

We can then use it:

```python
users = []

add_user(users, "Adam", 21)
add_user(users, "Lisa", 20, True)

print(users)
```

The function modifies the existing list.

---

# 10. Mutable Objects

Lists and dictionaries are mutable objects.

This means that their contents can be changed.

Example:

```python
def add_number(numbers):
    numbers.append(10)

numbers = [1, 2, 3]

add_number(numbers)

print(numbers)
```

Output:

```text
[1, 2, 3, 10]
```

The original list was modified.

The same concept applies to dictionaries:

```python
def update_user(user):
    user["age"] = 22

user = {
    "name": "Adam",
    "age": 21
}

update_user(user)

print(user)
```

Output:

```text
{
    "name": "Adam",
    "age": 22
}
```

---

# 11. Returning ```True``` or ```False```

A function can report whether an operation was successful.

Example:

```python
def update_user(users, name, new_age):
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            return True

    return False
```

If the user exists:

```python
success = update_user(users, "Lisa", 22)

print(success)
```

Output:

```text
True
```

If the user does not exist:

```python
success = update_user(users, "Peter", 30)

print(success)
```

Output:

```text
False
```

This pattern is extremely useful for larger programs.

---

# 12. Using ```return``` Inside a Loop

```return``` immediately ends the function.

Example:

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None
```

When the user is found:

```python
return user
```

immediately stops the function.

The loop does not continue.

This is different from ```break```.

```break```

Stops the loop:

```python
for user in users:
    if user["name"] == name:
        break
```

```return```

Stops the entire function:

```python
for user in users:
    if user["name"] == name:
        return user
```

---

# 13. Returning ```None```

```None``` represents the absence of a value.

It is commonly used when a function cannot find the requested object.

Example:

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None
```

Usage:

```python
user = find_user(users, "Lisa")

if user is not None:
    print(user)
else:
    print("User not found!")
```

This is a common Python pattern.

---

# 14. Adding Users

We can create a reusable function for adding users:

```python
def add_user(users, name, age, student=False):
    user = {
        "name": name,
        "age": age,
        "student": student
    }

    users.append(user)
```

Example:

```python
users = []

add_user(users, "Adam", 21)
add_user(users, "Lisa", 20, True)

print(users)
```

The function is responsible only for adding the user.

It does not load or save files.

This is an example of separation of responsibilities.

---

# 15. Updating Users

A function can search for a user and modify their data.

```python
def update_user(users, name, new_age):
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            return True

    return False
```

Usage:

```python
if update_user(users, "Lisa", 22):
    print("User updated!")
else:
    print("User not found!")
```

---

# 16. Deleting Users

To remove an entire dictionary from a list, we can use ```remove()```.

```python
def delete_user(users, name):
    for user in users:
        if user["name"] == name:
            users.remove(user)
            return True

    return False
```

Usage:

```python
if delete_user(users, "Andrew"):
    print("User deleted!")
else:
    print("User not found!")
```

### Important

```remove()``` removes an element from a list.

```python
users.remove(user)
```

This is different from:

```python
user.pop("city")
```

which removes a key from a dictionary.

---

# 17. Finding Users

A search function can return the matching dictionary:

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None
```

Usage:

```python
user = find_user(users, "Adam")

if user is not None:
    print(user)
else:
    print("User not found!")
```

---

# 18. Functions and JSON

Functions become especially useful when working with JSON files.

Instead of repeatedly writing:

```python
with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)
```

we can create a function:

```python
import json

def load_users(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
```

Now we can simply write:

```python
users = load_users("users.json")
```

---

# 19. Saving JSON Data

The same idea can be applied when saving.

```python
def save_users(filename, users):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)
```

Usage:

```python
save_users("users.json", users)
```

This keeps the file-handling logic in one place.

---

# 20. Separation of Responsibilities

One of the most important ideas from this lesson is that each function should have a clear responsibility.

For example:

```text
load_users()
    → loads data

save_users()
    → saves data

add_user()
    → adds a user

update_user()
    → updates a user

delete_user()
    → deletes a user

find_user()
    → finds a user
```

Instead of creating one huge block of code, we divide the program into smaller pieces.

This makes the program:

- easier to understand
- easier to debug
- easier to modify
- easier to reuse
- easier to test

---

# 21. CRUD

The functions we created form the basis of a CRUD system.

CRUD stands for:

```text
C → Create
R → Read
U → Update
D → Delete
```

Our functions correspond to:

```text
Create → add_user()
Read   → load_users() / find_user()
Update → update_user()
Delete → delete_user()
```

This pattern is extremely common in real applications.

---

# 22. Complete User Manager

Combining everything gives us:

```python
import json

def load_users(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_users(filename, users):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

def add_user(users, name, age, student=False):
    user = {
        "name": name,
        "age": age,
        "student": student
    }

    users.append(user)

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
```

Example usage:

```python
users = load_users("users.json")

add_user(users, "Emma", 24, True)

update_user(users, "Lisa", 22)

adam = find_user(users, "Adam")

if adam is not None:
    print(adam)

delete_user(users, "Andrew")

save_users("users.json", users)
```

---

# 23. Function Design Principles

When creating functions, keep these principles in mind.

## 1. Give functions one clear responsibility

Good:

```python
def load_users(filename):
    ...
```

Less ideal:

```python
def load_update_delete_and_print_users(filename):
    ...
```

A function should ideally do one logical job.

--- 

## 2. Use meaningful names

Good:

```python
def find_user(users, name):
```

Less clear:

```python
def f(x, y):
```

Function names should describe what the function does.

---

## 3. Use parameters instead of hardcoded values

Less flexible:

```python
def update_lisa(users):
    ...
```

More flexible:

```python
def update_user(users, name, new_age):
    ...
```

The second version can work with any user.

---

## 4. Return useful information

Instead of only printing:

```python
def find_user(users, name):
    print(user)
```

return the result:

```python
def find_user(users, name):
    return user
```

The caller can then decide what to do with the result.

---

# 24. Common Mistakes

## Forgetting ```return```

Incorrect:

```python
def load_users(filename):
    with open(filename) as file:
        users = json.load(file)
```

Correct:

```python
def load_users(filename):
    with open(filename) as file:
        return json.load(file)
```

Without ```return```, the function returns ```None```.

---

## Confusing ```print()``` and ```return```

```python
def get_name(user):
    print(user["name"])
```

is not equivalent to:

```python
def get_name(user):
    return user["name"]
```

The second version allows the caller to use the value.

---

## Using ```pop()``` when ```remove()``` is needed

For a list:

```python
users.remove(user)
```

For a dictionary:

```python
user.pop("city")
```

They solve different problems.

---

## Forgetting that ```return``` ends the function

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None
```

Once ```return user``` executes, the function immediately ends.

---

# 25. Key Takeaways

By the end of Day 06, you should understand:

- how to define functions using ```def```
- the difference between parameters and arguments
- how to use ```return```
- the difference between ```print()``` and ```return```
- how to use default parameters
- how functions work with lists and dictionaries
- how mutable objects can be modified inside functions
- how to return ```True``` and ```False```
- how to use ```None``` when no result exists
- how to use ```return``` inside loops
- how to organize JSON operations into functions
- how to separate responsibilities
- the basic idea of CRUD operations
- how functions can make programs smaller, cleaner, and reusable

---

# 🧠 Final Mental Model

A useful way to think about functions is:

```text
Input
  ↓
Function
  ↓
Processing
  ↓
Return value
```

For example:

```text
users + "Lisa" + 22
        ↓
   update_user()
        ↓
   find Lisa
        ↓
   change age
        ↓
      True
```

Functions allow us to turn a large program into small, understandable building blocks.

This concept will become increasingly important as projects become larger.