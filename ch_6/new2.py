a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2st number :"))
c = int(input("Enter the 3st number :"))

if(a>b):
    if(a>c):
        print("The largest number is :",a)
    else:
        print("The largest nymber is :",c)
elif(c>b):
    print("The largest numkber is :",c)
else:
    print("The largest number is :",b)
