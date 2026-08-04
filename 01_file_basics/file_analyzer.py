line_count = 0
character_count = 0

with open("notes.txt", encoding="utf-8") as file:

    for line in file:
        line_count += 1
        character_count += len(line.rstrip("\n"))


print(f"Lines: {line_count}")
print(f"Characters: {character_count}")