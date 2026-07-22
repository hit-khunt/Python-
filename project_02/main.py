from random import randint 

n = randint(1,100)

g=0
a = -1
while(a!=n):
    
    a = int(input("Enter a number : "))
    if(a>n):
        print("Guess Lower number please.")
        g += 1
    elif(a<n):
        print("Guess Higher number please")
        g += 1

print(f"You have Guess the correct number {n} in {g} number of guesses.")