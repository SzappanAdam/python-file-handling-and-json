# Without newline characters

languages = [
    "Python",
    "Java",
    "C#",
    "JavaScript"
]

with open("languages_without_newlines.txt", "w", encoding="utf-8") as file:
    file.writelines(languages)


# With newline characters

languages = [
    "Python\n",
    "Java\n",
    "C#\n",
    "JavaScript"
]

with open("languages_with_newlines.txt", "w", encoding="utf-8") as file:
    file.writelines(languages)