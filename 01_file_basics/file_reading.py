# Basic file reading examples

# Old approach
file = open("notes.txt", encoding="utf-8")

content = file.read()

print(content)

file.close()


print("----------------")


# Recommended approach
with open("notes.txt", encoding="utf-8") as file:
    content = file.read()

print(content)