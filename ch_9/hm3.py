# For one word
'''
word = "donkey"

with open("file1.txt") as f:
    content = f.read()

newcontent = content.replace(word, "******")

with open("file1.txt", "w") as f:
    f.write(newcontent)
'''
# For many words

words = ["bad","beats","killed","donkey"]

with open("file1.txt") as f:
    contant = f.read()

for word in words:
    contant = contant.replace(word, "*"*len(word))

with open("file1.txt", "w") as f:
    f.write(contant)