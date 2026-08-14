# Day 04 — Modifying JSON Data

Today we learned how to work with JSON data after loading it into Python.

The main idea of this lesson was:

```text
JSON file
    ↓
json.load()
    ↓
Python data structure
    ↓
modify / add / delete / search
    ↓
json.dump()
    ↓
JSON file
```

---

## 1. Loading JSON Data

We can load JSON data from a file using ```json.load()```.

```python
import json


with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)
```

After loading, ```user``` is a normal Python data structure.

For example, a JSON object becomes a Python dictionary:

```JSON
{
    "name": "Adam",
    "age": 21
}
```

becomes:

```python
{
    "name": "Adam",
    "age": 21
}
```

We can now use normal Python dictionary operations.

---

## 2. Modifying Existing Values

We can modify an existing dictionary value using its key.

```python
user["age"] = 22
```

If the key already exists, its value is replaced.

Example:

```python
user = {
    "name": "Adam",
    "age": 21
}

user["age"] = 22
```

Result:

```python
{
    "name": "Adam",
    "age": 22
}
```

---

## 3. Adding New Keys

If a key does not exist, assigning a value creates a new key-value pair.

```python
user["city"] = "Budapest"
```

Example:

```python
user = {
    "name": "Adam",
    "age": 22
}

user["city"] = "Budapest"
```

Result:

```python
{
    "name": "Adam",
    "age": 22,
    "city": "Budapest"
}
```

The same syntax is used for both modifying and adding data.

```python
user["age"] = 22
```

Modifies an existing key.

```python
user["city"] = "Budapest"
```

Creates a new key if it does not exist.

---

## 4. Deleting Dictionary Data with ```del```

The ```del``` keyword can remove a key-value pair from a dictionary.

```python
del user["city"]
```

Example:

```python
user = {
    "name": "Adam",
    "age": 22,
    "city": "Budapest"
}

del user["city"]
```

Result:

```python
{
    "name": "Adam",
    "age": 22
}
```

### Important

If the key does not exist, ```del``` raises a ```KeyError```.

```python
del user["country"]
```

If ```"country"``` does not exist:

```text
KeyError
```

We can avoid this by checking first:

```python
if "country" in user:
    del user["country"]
```

---

## 5. The ```in``` Operator with Dictionaries

When used with a dictionary, ```in``` checks whether a key exists.

```python
if "student" in user:
    ...
```

Example:

```python
user = {
    "name": "Adam",
    "age": 21
}

print("name" in user)
```

Output:

```text
True
```

But:

```python
print("Adam" in user)
```

returns:

```text
False
```

because ```"Adam"``` is a value, not a key.

---

## 6. The ```pop()``` Method

```pop()``` removes a key-value pair and returns the removed value.

```python
city = user.pop("city")
```

Example:

```python
user = {
    "name": "Adam",
    "age": 22,
    "city": "Budapest"
}

removed_city = user.pop("city")

print(removed_city)
print(user)
```

Output:

```text
Budapest
{'name': 'Adam', 'age': 22}
```

Therefore:

```python
del user["city"]
```

only deletes the key.

While:

```python
city = user.pop("city")
```

deletes the key and gives us the removed value.

---

## 7. Safe ```pop()```

By default, ```pop()``` raises a ```KeyError``` if the key does not exist.

```python
user.pop("city")
```

If ```"city"``` is missing:

```text
KeyError
```

We can provide a default value:

```python
city = user.pop("city", None)
```

If ```"city"``` exists:

```python
city == "Budapest"
```

If ```"city"``` does not exist:

```python
city == None
```

Another example:

```python
removed = user.pop("city", "Unknown")
```

If the key does not exist:

```python
removed == "Unknown"
```

The default value is only returned. It does not create the missing key.

---

## 8. Lists of Dictionaries

JSON data often contains a list of objects.

Example:

```JSOn
[
    {
        "name": "Adam",
        "age": 21
    },
    {
        "name": "Lisa",
        "age": 20
    }
]
```

After loading:

```python
users = json.load(file)
```

we get:

```text
list
├── dictionary
└── dictionary
```

We can iterate through the users:

```python
for user in users:
    print(user["name"])
```

---

## 9. Searching for a User

We can search through a list of dictionaries using a ```for``` loop and an ```if``` statement.

```python
for user in users:
    if user["name"] == "Lisa":
        user["age"] = 21
```

This finds Lisa and modifies her age.

We should generally search based on data rather than assuming a fixed list position.

Less flexible:

```python
users[1]["age"] = 21
```

More flexible:

```python
for user in users:
    if user["name"] == "Lisa":
        user["age"] = 21
```

---

## 10. Conditional Updates

We can modify only users who satisfy a condition.

Example:

```python
for user in users:
    if user["student"]:
        user["age"] += 1
```

This increases the age only for users whose ```student``` value is ```True```.

Because ```student``` is already a Boolean, this is preferred:

```python
if user["student"]:
```

instead of:

```python
if user["student"] == True:
```

---

## 11. Adding a New User

If the JSON contains a list of users, we can add a new dictionary using ```append()```.

```python
new_user = {
    "name": "Andrew",
    "age": 34,
    "student": False
}

users.append(new_user)
```

The new dictionary becomes another element of the list.

Example:

```python
users = [
    {"name": "Adam", "age": 21},
    {"name": "Lisa", "age": 20}
]

new_user = {
    "name": "Andrew",
    "age": 34
}

users.append(new_user)
```

Result:

```python
[
    {"name": "Adam", "age": 21},
    {"name": "Lisa", "age": 20},
    {"name": "Andrew", "age": 34}
]
```

---

## 12. Saving Modified Data

After modifying the Python data structure, we need to save it back to the JSON file.

```python
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)
```

The complete workflow is:

```python
with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)

user["age"] = 22

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)
```

The important concept is:

```text
load → modify → dump
```

---

## 13. ```load()``` and ```dump()``` in a File Workflow

For files:

```python
json.load(file)
```

reads JSON from a file and converts it into a Python object.

```python
json.dump(data, file)
```

takes a Python object and writes it to a file as JSON.

Therefore:

```text
json.load()
JSON file → Python object

json.dump()
Python object → JSON file
```

---

## 14. JSON Must Contain One Valid JSON Document

A JSON file should contain one complete JSON document.

This is incorrect:

```python
json.dump(users, file)
json.dump(student_count, file)
```

The first ```dump()``` already writes a complete JSON structure.

Writing another JSON value directly after it produces invalid JSON.

Conceptually, the file could become:

```text
[{"name": "Adam"}]3
```

This is not one valid JSON document.

If multiple pieces of information need to be stored, they should be part of one JSON structure.

For example:

```python
data = {
    "users": users,
    "active_students": student_count
}

json.dump(data, file, indent=4)
```

This produces valid JSON:

```JSON
{
    "users": [
        {
            "name": "Adam"
        }
    ],
    "active_students": 1
}
```

---

## 15. Calculated Values vs Stored Data

Not every Python variable needs to be saved into the JSON file.

For example:

```python
student_count = 0


for user in users:
    if user["student"]:
        student_count += 1
```

```student_count``` can simply be a calculated result.

We can display it:

```python
print(f"Active students: {student_count}")
```

without putting it into the JSON file.

The important question is:

Is this information part of the data we want to store, or is it only a temporary calculation?

---

## 16. Complete Example

The following program combines the concepts learned today:

```python
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
    if user["student"]:
        user["age"] += 1
        user["active"] = True
        student_count += 1

    if user["name"] == "Andrew":
        user.pop("student", None)

with open("users.json", "w", encoding="utf-8") as file:
    json.dump(users, file, indent=4)

print(f"Active students: {student_count}")

with open("users.json", "r", encoding="utf-8") as file:
    print(json.load(file))
```

This combines:

- JSON loading
- JSON saving
- list manipulation
- dictionary manipulation
- searching
- conditional updates
- adding data
- deleting data
- safe pop()
- counting data
- formatted JSON output

---

## 17. The Complete Mental Model

When working with JSON files in Python, think about the process like this:

```text
             JSON FILE
                 │
                 │ json.load()
                 ▼
        Python list / dictionary
                 │
        ┌────────┼─────────┐
        │        │         │
      READ     MODIFY    DELETE
        │        │         │
        └────────┼─────────┘
                 │
              ADD DATA
                 │
                 ▼
        Python list / dictionary
                 │
                 │ json.dump()
                 ▼
             JSON FILE
```

The JSON file is the persistent storage.

The Python data structure is where we perform the actual data manipulation.

---

## Key Takeaways
### ```json.load()```

```python
data = json.load(file)
```

File → Python object.

### ```json.dump()```

```python
json.dump(data, file, indent=4)
```

Python object → JSON file.

### Modify

```python
user["age"] = 22
```

### Add

```python
user["city"] = "Budapest"
```

### Delete

```python
del user["city"]
```

### Safe delete

```python
if "city" in user:
    del user["city"]
```

### Remove and return value

```python
city = user.pop("city")
```

### Safe ```pop()```

```python
city = user.pop("city", None)
```

### Add an item to a list

```python
users.append(new_user)
```

### Search

```python
for user in users:
    if user["name"] == "Lisa":
        ...
```

### Conditional update
```python
for user in users:
    if user["student"]:
        user["age"] += 1
```

---

## Day 04 Summary

Today we moved beyond simply reading JSON.

We learned how to treat a JSON file as persistent data that can be loaded into Python, manipulated using normal Python data structures, and then saved back to the file.

The central pattern is:

```text
READ → MODIFY → WRITE
```

or, more specifically:

```text
json.load()
    ↓
Python data
    ↓
Python operations
    ↓
json.dump()
```

This pattern is fundamental to many small applications that use files as their data storage.