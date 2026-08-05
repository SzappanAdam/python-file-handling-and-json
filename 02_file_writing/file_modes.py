# x mode creates a file only if it does not exist

with open("new_file.txt", "x", encoding="utf-8") as file:
    file.write("Hello")