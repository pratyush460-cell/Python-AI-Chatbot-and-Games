marks = {
    "Parle": 100,
    "Patte": 56,
    "Pratyush": 23,
    0: "Parle"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Parle": 99, "Renuka": 100})
# print(marks)

print(marks.get("Parle2")) # Prints None
print(marks["Parle2"]) # Returns an error