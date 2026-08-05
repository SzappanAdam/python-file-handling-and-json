# Python File Writing Fundamentals

## 1. Introduction

In Python, files can be opened using the built-in `open()` function.

General syntax:

```python
file = open("filename", "mode")
```

A recommended approach is using a context manager:

```python
with open("filename", "mode", encoding="utf-8") as file:
    # file operations
```

The with statement automatically closes the file after the block finishes.

---

## 2. File Modes

The mode determines what operations can be performed on the file.

Mode	Description	Existing file	Missing file
r	Read	Opens file	Error
w	Write	Clears content and writes	Creates file
a	Append	Adds content at the end	Creates file
x	Exclusive creation	Error	Creates file

---

## 3. Write Mode (w)

The "w" mode is used when we want to write new content.

Example:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python")
```

Important:

The file is cleared immediately when opened.

Example:

Before:

```text
Python
JSON
GitHub
```

Code:

```python
with open("notes.txt", "w") as file:
    file.write("Hello")
```

After:

```text
Hello
```

The previous content is lost.

---

## 4. Append Mode (a)

The "a" mode adds new content to the end of the file.

Example:

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("New event\n")
```

Before:

```text
Program started
```

After:

```text
Program started
New event
```

Unlike "w", existing data is preserved.

---

## 5. Write Method

The write() method writes a string into a file.

Example:

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

The return value is the number of characters written.

Example:

```python
result = file.write("Hello")

print(result)
```

Output:

```text
5
```

because "Hello" contains five characters.

The newline character (\n) is also counted.

Example:

```python
file.write("Hello\n")
```

Result:

```text
6
```

---

## 6. Multiple write Operations

Multiple write() calls continue from the current file position.

Example:

```python
with open("notes.txt", "w") as file:
    file.write("Hello")
    file.write("World")
```

Result:

```text
HelloWorld
```

The write() method does not automatically create new lines.

To create a new line:

```python
file.write("Hello\n")
file.write("World")
```

Result:

```text
Hello
World
```

---

## 7. writelines()

The writelines() method writes multiple strings from an iterable.

Example:

```python
languages = [
    "Python\n",
    "Java\n",
    "C#"
]

with open("languages.txt", "w") as file:
    file.writelines(languages)
```

Result:

```text
Python
Java
C#
```

Important:

writelines() does NOT automatically add newline characters.

This:

```python
languages = [
    "Python",
    "Java",
    "C#"
]
```

creates:

```text
PythonJavaC#
```

because Python writes the strings exactly as provided.

---

## 8. Common Mistakes

Forgetting newline characters

Wrong:

```python
file.write("Python")
file.write("Java")
```

Result:

```text
PythonJava
```

Correct:

```python
file.write("Python\n")
file.write("Java")
```

### Using "w" accidentally

Example:

```python
open("important.txt", "w")
```

This immediately deletes the previous content.

Always check the mode before writing.

---

## 9. Practical Example: Log File

A common use case is creating application logs.

Example:

```python
logs = [
    "Application started\n",
    "User logged in\n"
]

with open("application.log", "w") as file:
    file.writelines(logs)

with open("application.log", "a") as file:
    file.write("User logged out\n")
```

Final file:

```text
Application started
User logged in
User logged out
```

### Summary

Important concepts:

- "w" creates or overwrites files.
- "a" adds content without deleting existing data.
- write() writes one string.
- writelines() writes multiple strings.
- Python does not automatically add new lines.
- \n must be added manually.
- write() returns the number of written characters.
- The file pointer determines where new content is written.

---