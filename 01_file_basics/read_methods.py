# Demonstrating read methods

with open("notes.txt", encoding="utf-8") as file:

    print("READ:")
    file.seek(0)
    print(file.read())


    print("\nREADLINE:")
    file.seek(0)
    print(file.readline())


    print("\nREADLINES:")
    file.seek(0)
    print(file.readlines())