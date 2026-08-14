try:
    age = int("21")

except ValueError:
    print("Invalid age!")

finally:
    print("This always runs!")

try:
    age = int("twenty")

except ValueError:
    print("Invalid age!")

finally:
    print("This always runs!")


##
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File successfully opened!")
finally:
    print("Operation finished!")