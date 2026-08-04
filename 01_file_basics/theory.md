# File Handling Fundamentals

## What is file handling?

Variables in Python exist only while the program is running.
When the program stops, data stored in memory is lost.

Files allow us to store data permanently on disk.

Examples:

- txt files
- JSON files
- CSV files
- databases

---

## How Python communicates with files

Python does not directly access the storage device.

The process:

Python program
↓
open()
↓
File object
↓
Operating System
↓
File system
↓
Storage device


The file object is a Python object that allows communication with the file.

---

## Opening a file

Basic syntax:

```python
file = open("filename.txt")
```

However, the recommended modern approach is:

```python
with open("filename.txt", encoding="utf-8") as file:
    content = file.read()
```

The with statement automatically closes the file.

---

## File closing

Manual approach:

```python
file = open("notes.txt")

content = file.read()

file.close()
```

The problem:

If an error happens before close(), the file may remain open.

Using with avoids this problem.

---

## Reading files

```python
read()
```

Reads the remaining content of the file.

Example:

```python
content = file.read()
```

The whole content is returned as a string.

```python
readline()
```

Reads one line from the current position.

Example:

```python
line = file.readline()
readlines()
```

Reads all remaining lines and returns them as a list.

Example:

```python
lines = file.readlines()
```

---

## File pointer

A file has a current position called the file pointer.

Example:

```python
content = file.read()
```

After reading, the pointer moves to the end of the file.

Calling:

```python
file.read()
```

again returns:

```python
""
```

because there is nothing left to read.

Moving the file pointer

The seek() method changes the current position.

Example:

```python
file.seek(0)
```

Moves the pointer back to the beginning.

## Iterating through files

Files can be processed line by line:

```python
with open("users.txt") as file:
    for line in file:
        print(line)
```

Advantages:

lower memory usage
works with very large files
processes data step by step

---

## Memory considerations

Avoid:

```python
data = file.read()
```

for very large files.

The whole file is loaded into memory.

Better:

```python
for line in file:
    process(line)
```

Only a small part is handled at a time.

---

## Practice tasks

### file_reading.py

Topics:

- open()
- read()
- with statement

### read_methods.py

Topics:

- read()
- readline()
- readlines()
- seek()

### file_analyzer.py

Topics:

- file iteration
- counting lines
- counting characters
- len()
- strip()