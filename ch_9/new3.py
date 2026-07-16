f = open("myfile.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("myfile.txt") as f:
    print(f.read())

# you dont have to explicitly close the file 