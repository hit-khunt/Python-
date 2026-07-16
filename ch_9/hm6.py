with open("file.txt") as f:
    file = f.read()

with open("file2.txt", "w") as f:
    f.write(file)