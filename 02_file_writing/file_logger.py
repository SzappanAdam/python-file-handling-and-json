logs = [
    "Program started\n",
    "User logged in\n",
    "File uploaded\n"
]

# Create initial log entries

with open("application.log", "w", encoding="utf-8") as file:
    file.writelines(logs)


# Append a new event

with open("application.log", "a", encoding="utf-8") as file:
    file.write("User logged out\n")


with open("application.log", "r", encoding="utf-8") as file:
    print(file.read())