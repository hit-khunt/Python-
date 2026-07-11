a = int(input("Enter your Age :"))

if(a>=18):
    print("you are aligible for voting.")
    print("Thanks for visit")

elif(a<0):
    print("invalid input.")
    print("please enter valid input")

elif(a==0):
    print("invalid input.")
    print("please enter valid input")

else:
    print("you are not aligible for voting.")
    print("Sorry")

print("end of the program.")