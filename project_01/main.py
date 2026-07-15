import random
'''
1 for rock
-1 for paper
0 for scissors
'''

computer = random.choice([-1,0,1])
print('''r for rock
p for paper
s for scissor      
''')
your = input("Enter your choice from r,p,s : ").lower()
dict={"r":1, "p":-1, "s":0}
revdict={1:"roke", -1:"paper", 0:"scissor"}

if your not in dict:
    print("Invalid choice!")
    exit()
    
you = dict[your]

print(f"your choice {revdict[you]} and computers choice {revdict[computer]}")

# if(computer==you):
#     print("it's tie(draw)")
# elif(computer==1 and you ==-1):
#     print("you win!")
# elif(computer==-1 and you ==1):
#     print("you lose!")
# elif(computer==1 and you ==0):
#     print("you lose!")
# elif(computer==-1 and you ==0):
#     print("you win!")
# elif(computer==0 and you ==1):
#     print("you win!")
# elif(computer==0 and you ==-1):
#     print("you lose!")

win = [(1, 0), (-1, 1), (0, -1) ]

if computer == you:
    print("It's a tie!")
elif(you,computer) in win:
    print("You win!")
else:
    print("You lose!")