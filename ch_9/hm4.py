with open("log.txt") as f:
    contant = f.read()

if "python" in contant:
    print("Yes")
else:
    print("No")