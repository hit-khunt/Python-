with open("myfile.txt") as f:
    c = f.read()
    a = "Hello!"
    if a in c:
        print("The Hello! word is in the file.")
    else:
        print("The Hello! word is not in the file.")