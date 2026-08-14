# Day 05 — Exception Handling & Validation

## 1. Introduction

Programs often encounter unexpected situations:

- a file does not exist
- a JSON file contains invalid data
- a dictionary key is missing
- a value has an invalid format
- an operation is performed on incompatible types

Python provides exception handling to prevent these errors from unnecessarily terminating a program.

The main tools are:

- `try`
- `except`
- `else`
- `finally`
- `raise`

---

# 2. The `try` Statement

Code that might cause an exception can be placed inside a `try` block.

```python
try:
    age = int("twenty")
```

If an exception occurs, Python looks for a matching ```except``` block.

---

## 3. The ```except``` Statement

```except``` is used to handle a specific exception.

```python
try:
    age = int("twenty")

except ValueError:
    print("Invalid age!")
```

Instead of terminating the program immediately, Python executes the matching ```except``` block.

---

## 4. Multiple Exceptions

Different problems can produce different exceptions.

```python
try:
    with open("user.json", "r", encoding="utf-8") as file:
        user = json.load(file)

except FileNotFoundError:
    print("File not found!")

except json.JSONDecodeError:
    print("Invalid JSON!")

except KeyError:
    print("Missing key!")
```

This makes error handling more precise and easier to debug.

---

## 5. Important Exceptions

### FileNotFoundError

Occurs when trying to open a file that does not exist.

```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found!")
```

### JSONDecodeError

Occurs when Python tries to load invalid JSON.

```python
import json

try:
    with open("user.json", "r") as file:
        user = json.load(file)

except json.JSONDecodeError:
    print("Invalid JSON!")
```

### KeyError

Occurs when trying to access a dictionary key that does not exist.

```python
user = {
    "name": "Adam"
}

try:
    print(user["age"])


except KeyError:
    print("Age key does not exist!")
```

### ValueError

Occurs when the type of an argument is appropriate, but its value is invalid.

```python
try:
    age = int("twenty")

except ValueError:
    print("Invalid age!")
```

The string is a valid ```str```, but ```"twenty"``` cannot be converted into an integer.

### TypeError

Occurs when an operation is performed on incompatible types.

```python
age = "21"

try:
    result = age + 5

except TypeError:
    print("Incompatible types!")
```

### Important distinction

```text
ValueError → correct type, invalid value
TypeError → incompatible type
```

---

## 6. The ```else``` Block

The ```else``` block runs only when the ```try``` block completes without an exception.

```python
try:
    age = int("21")

except ValueError:
    print("Invalid age!")

else:
    print("Age successfully converted!")
```

The ```else``` block is useful for code that should only execute after successful processing.

---

## 7. The ```finally``` Block

The ```finally``` block runs regardless of whether an exception occurred.

```python
try:
    age = int("twenty")

except ValueError:
    print("Invalid age!")

finally:
    print("Operation finished!")
```

Output:

```text
Invalid age!
Operation finished!
```

A common structure is:

```python
try:
    # operation

except SomeError:
    # handle error

else:
    # execute if successful

finally:
    # always execute
```

---

## 8. Using ```as``` with Exceptions

An exception can be stored in a variable using ```as```.

```python
try:
    age = int("twenty")

except ValueError as error:
    print(error)
```

This allows us to access the exception object and its message.

---

## 9. The ```raise``` Statement

```raise``` allows us to manually create an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative!")
```

This is useful when the data is technically valid Python data, but violates a rule defined by our program.

For example:

```python
age = -5
```

is a valid integer, but a negative age may not be valid according to our application's rules.

---

## 10. Combining ```raise``` and ```except```

We can raise our own exception and then handle it.

```python
age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative!")

except ValueError as error:
    print(error)
```

Output:

```text
Age cannot be negative!
```

---

## 11. Validation

Validation means checking whether data satisfies the rules required by our program.

Example:

```python
user = {
    "name": "Adam",
    "age": 21,
    "student": True
}

try:
    name = user["name"]
    age = user["age"]
    student = user["student"]

    if age < 0:
        raise ValueError("Age cannot be negative!")

except KeyError:
    print("Required key is missing!")

except ValueError as error:
    print(error)

else:
    print("User data is valid!")
```

Validation is especially important when working with:

- JSON files
- user input
- APIs
- databases
- configuration files

---

## 12. Why Bare ```except``` Is Usually a Bad Idea

Avoid using:

```python
try:
    ...
except:
    print("Something went wrong")
```

A bare ```except``` catches almost every exception.

This makes debugging much harder because we lose information about what actually went wrong.

Prefer specific exceptions:

```python
except FileNotFoundError:
    ...

except json.JSONDecodeError:
    ...

except KeyError:
    ...

except ValueError:
    ...
```

Specific exception handling makes programs easier to understand, maintain, and debug.

---

## 13. Common Exception Handling Structure

A common pattern is:

```python
try:
    # risky operation

except SpecificError:
    # handle specific error

else:
    # successful operation

finally:
    # cleanup / always executed
```

Not every program needs all four parts.

Use only the parts that make sense for the situation.

---

## 14. JSON + File Handling + Exception Handling

These concepts can be combined to safely work with JSON files.

```python
import json

try:
    with open("user.json", "r", encoding="utf-8") as file:
        user = json.load(file)

    age = user["age"]

    if age < 0:
        raise ValueError("Age cannot be negative!")

except FileNotFoundError:
    print("File not found!")

except json.JSONDecodeError:
    print("Invalid JSON!")

except KeyError:
    print("Age key does not exist!")

except ValueError as error:
    print(error)

else:
    print("User data is valid!")

finally:
    print("Validation finished.")
```

This combines:

- file handling
- JSON loading
- dictionary access
- exception handling
- validation
- custom exceptions

---

## 15. Key Takeaways

### ```try```

Contains code that might raise an exception.

### ```except```

Handles an exception.

### ```else```

Runs when the ```try``` block succeeds.

### ```finally```

Runs regardless of success or failure.

### ```raise```

Manually raises an exception.

### ```as```

Stores the exception object in a variable.

---

## 16. Exception Summary

Exception	Typical situation
```FileNotFoundError```	File does not exist
```JSONDecodeError```	Invalid JSON
```KeyError```	Missing dictionary key
```ValueError```	Invalid value
```TypeError```	Incompatible types

---

## 17. Important Mental Model

Remember:

```text
try
 │
 ├── exception ──→ except
 │
 └── no exception ──→ else
                          │
                          ▼
                       finally
                          │
                          ▼
                    program continues
```

The goal of exception handling is not simply to hide errors.

The goal is to:

1. Detect unexpected situations.
2. Understand what went wrong.
3. Handle known problems appropriately.
4. Keep the program stable when possible.
5. Make debugging easier.