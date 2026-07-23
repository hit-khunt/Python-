from random import randint

name = input("Enter your name : ")
number = int(input("Enter phone Number : "))
score = randint(0,100)

s = "The name of the student is {}, His score is {} and phone number is {}".format(name, score, number)

print(s)