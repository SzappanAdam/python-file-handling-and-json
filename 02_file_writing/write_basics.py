with open("notes.txt", "w", encoding="utf-8") as file:
    results = []

    results.append(file.write("Python\n"))
    results.append(file.write("JSON\n"))
    results.append(file.write("GitHub"))

print(results)


with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello")


with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())