# Day 03 — JSON

## 1. What is JSON?

JSON stands for **JavaScript Object Notation**.

It is a lightweight text-based data format commonly used for:

* storing data
* configuration files
* APIs
* communication between applications
* exchanging structured data

Example:

```json
{
    "name": "Adam",
    "age": 21,
    "student": true
}
```

JSON is **not Python code**. It is a data representation format.

In Python:

```python
user = {
    "name": "Adam",
    "age": 21
}
```

`user` is a Python variable name.

In JSON:

```json
{
    "name": "Adam",
    "age": 21
}
```

There is no variable name. The JSON contains only the data.

---

# 2. Python and JSON data types

Python and JSON have corresponding data types.

| Python          | JSON    |
| --------------- | ------- |
| `dict`          | object  |
| `list`          | array   |
| `str`           | string  |
| `int` / `float` | number  |
| `True`          | `true`  |
| `False`         | `false` |
| `None`          | `null`  |

Example:

```python
user = {
    "name": "Adam",
    "age": 21,
    "student": True,
    "languages": ["Python", "SQL"]
}
```

JSON representation:

```json
{
    "name": "Adam",
    "age": 21,
    "student": true,
    "languages": ["Python", "SQL"]
}
```

Notice that Python uses:

```python
True
```

while JSON uses:

```json
true
```

---

# 3. The `json` module

Python provides the built-in `json` module for working with JSON.

```python
import json
```

The four most important functions are:

```python
json.dumps()
json.loads()

json.dump()
json.load()
```

---

# 4. `json.dumps()`

`json.dumps()` converts a Python object into a JSON string.

Example:

```python
import json

user = {
    "name": "Adam",
    "age": 21,
    "student": True
}

json_data = json.dumps(user)

print(json_data)
print(type(json_data))
```

Result:

```text
{"name": "Adam", "age": 21, "student": true}
<class 'str'>
```

The important point:

```text
Python object
      ↓
  json.dumps()
      ↓
  JSON string
```

The `s` in `dumps` can be remembered as:

> **s = string**

---

# 5. `json.loads()`

`json.loads()` does the opposite of `json.dumps()`.

It converts a JSON string into a Python object.

Example:

```python
json_data = '{"name": "Adam", "age": 21, "student": true}'

user = json.loads(json_data)

print(user)
print(type(user))
```

Result:

```text
{'name': 'Adam', 'age': 21, 'student': True}
<class 'dict'>
```

The process:

```text
JSON string
     ↓
 json.loads()
     ↓
Python object
```

Because the input is a string, `loads()` contains the `s`.

---

# 6. `json.dump()`

`json.dump()` writes a Python object directly into a file in JSON format.

Example:

```python
user = {
    "name": "Adam",
    "age": 21,
    "student": True
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)
```

The process:

```text
Python object
     ↓
 json.dump()
     ↓
 JSON file
```

Unlike `dumps()`, `dump()` works directly with a file object.

---

# 7. `json.load()`

`json.load()` reads JSON data from a file and converts it into a Python object.

Example:

```python
with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)
```

The process:

```text
JSON file
    ↓
json.load()
    ↓
Python object
```

If the JSON represents an object, the result will usually be a Python `dict`.

---

# 8. `dump` vs `dumps` and `load` vs `loads`

This is one of the most important things to remember.

```text
dumps → Python → JSON string
loads → JSON string → Python

dump  → Python → JSON file
load  → JSON file → Python
```

The easiest memory trick:

> **`s` = string**

| Function       | Input                | Output        |
| -------------- | -------------------- | ------------- |
| `json.dumps()` | Python object        | JSON string   |
| `json.loads()` | JSON string          | Python object |
| `json.dump()`  | Python object + file | JSON file     |
| `json.load()`  | JSON file            | Python object |

---

# 9. `read()` vs `json.load()`

These are not the same.

Suppose `user.json` contains:

```json
{
    "name": "Adam",
    "age": 21
}
```

Using:

```python
with open("user.json", "r", encoding="utf-8") as file:
    data = file.read()
```

produces:

```python
str
```

`read()` simply reads the file contents as text.

It does not know that the text contains JSON.

To convert that string into a Python object:

```python
data = json.loads(data)
```

This requires two steps:

```python
with open("user.json", "r", encoding="utf-8") as file:
    data = file.read()

data = json.loads(data)
```

But `json.load()` can perform the JSON loading directly:

```python
with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

Therefore:

```text
read()
  ↓
file → str

json.loads()
  ↓
JSON str → Python object
```

while:

```text
json.load()
  ↓
JSON file → Python object
```

---

# 10. JSON arrays and multiple objects

A JSON file can contain multiple objects by placing them inside an array.

Valid JSON:

```json
[
    {
        "name": "Adam",
        "age": 21
    },
    {
        "name": "Anna",
        "age": 22
    },
    {
        "name": "Peter",
        "age": 20
    }
]
```

In Python, this corresponds to:

```python
users = [
    {"name": "Adam", "age": 21},
    {"name": "Anna", "age": 22},
    {"name": "Peter", "age": 20}
]
```

The Python structure is:

```text
list
├── dict
├── dict
└── dict
```

Multiple separate JSON objects cannot simply be placed next to each other:

```json
{"name": "Adam"}
{"name": "Anna"}
```

That is not valid JSON.

They need to be contained inside a common JSON array.

---

# 11. Nested JSON data

Real-world JSON is often more complex.

Example:

```python
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
    }
]
```

The structure is:

```text
list
│
├── dict
│   ├── name → str
│   ├── age → int
│   ├── student → bool
│   └── languages → list
│                     ├── str
│                     └── str
│
└── dict
    ├── name → str
    ├── age → int
    ├── student → bool
    └── languages → list
```

We can access nested values using multiple indexing operations:

```python
users[0]["name"]
```

or:

```python
users[0]["languages"]
```

---

# 12. Iterating through nested data

A `for` loop can be used to process every dictionary in the list.

```python
for user in users:
    print(user["name"])
```

To process the languages as well:

```python
for user in users:
    for language in user["languages"]:
        print(language)
```

This is called nested iteration.

---

# 13. `join()`

`join()` combines string elements from an iterable into one string.

Example:

```python
languages = ["Python", "SQL"]

result = ", ".join(languages)

print(result)
```

Output:

```text
Python, SQL
```

The string before `.join()` is the separator.

Examples:

```python
" - ".join(["Python", "SQL", "Git"])
```

Result:

```text
Python - SQL - Git
```

Another example:

```python
" | ".join(["Python", "SQL", "Git"])
```

Result:

```text
Python | SQL | Git
```

Nested JSON data can therefore be displayed cleanly:

```python
for user in users:
    result = ", ".join(user["languages"])
    print(user["name"], "->", result)
```

---

# 14. Formatting JSON with `indent`

JSON can be written in a compact form:

```json
{"name": "Adam", "age": 21, "student": true}
```

For better readability, `indent` can be used:

```python
json.dump(user, file, indent=4)
```

This produces:

```json
{
    "name": "Adam",
    "age": 21,
    "student": true
}
```

`indent=4` means that each nested level uses four spaces.

This is especially useful when JSON files are intended to be read or edited by humans.

---

# 15. JSON errors

JSON data must follow valid JSON syntax.

For example, this is invalid:

```json
{
    "name": "Adam",
    "age": 21,
    "student": true,
}
```

There is an extra comma after the last property.

Trying to load invalid JSON can raise:

```python
json.JSONDecodeError
```

We can handle this with `try` and `except`:

```python
import json

try:
    with open("user.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("JSON successfully loaded!")

except json.JSONDecodeError:
    print("Invalid JSON!")
```

This allows the program to handle invalid JSON without crashing.

---

# 16. JSON and file persistence

JSON is useful because data stored in a JSON file remains available after the Python program terminates.

For example:

```text
Python program
      ↓
Python dictionary
      ↓
json.dump()
      ↓
user.json
      ↓
program closes
```

Later:

```text
program starts again
      ↓
json.load()
      ↓
Python dictionary
```

This is a basic form of data persistence.

---

# 17. Important concepts to remember

### Serialization

Converting a Python object into JSON representation:

```text
Python → JSON
```

For example:

```python
json.dumps()
json.dump()
```

### Deserialization

Converting JSON back into a Python object:

```text
JSON → Python
```

For example:

```python
json.loads()
json.load()
```

---

# 18. Quick reference

```python
# Python → JSON string
json.dumps(data)

# JSON string → Python
json.loads(data)

# Python → JSON file
json.dump(data, file)

# JSON file → Python
json.load(file)
```

Remember:

```text
        STRING          FILE

→ JSON   dumps()        dump()

→ Python loads()        load()
```

And:

> **`s` = string**

---

# Day 03 checklist

* [x] Understand what JSON is
* [x] Understand Python ↔ JSON data types
* [x] Use `json.dumps()`
* [x] Use `json.loads()`
* [x] Use `json.dump()`
* [x] Use `json.load()`
* [x] Understand the `s` distinction
* [x] Read JSON files
* [x] Write JSON files
* [x] Work with lists of dictionaries
* [x] Work with nested data
* [x] Iterate through nested data
* [x] Use `join()`
* [x] Format JSON with `indent`
* [x] Handle `JSONDecodeError`
* [x] Understand basic data persistence

**Day 03 status: COMPLETE**
