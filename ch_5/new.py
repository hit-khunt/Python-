# Dictionary {}
marks = {
    "Heet" : 99,
    "Mihir" : 67,
    "Yash" : 56
}
print(marks)

print(len(marks))
print(marks["Heet"]) # if false returs an error
print(marks.get("Heet")) # if false prints none

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Heet" : 85, "Hit" : 98})
print(marks)

print(len(marks))