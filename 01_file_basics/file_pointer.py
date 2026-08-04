# Checking if file closes automatically

with open("notes.txt", encoding="utf-8") as file:
    print(file.closed)

print(file.closed)


print("----------------")


# File pointer example

with open("notes.txt", encoding="utf-8") as file:
    first = file.read()
    second = file.read()

print(repr(first))
print(repr(second))


print("----------------")


# Moving pointer back

with open("notes.txt", encoding="utf-8") as file:
    first = file.read()

    file.seek(0)

    second = file.read()

print(first)
print(second)