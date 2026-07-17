n = int(input("Enter the number : "))

for i in range(1,n+1): 
    if(i == 1 or i==n or i==2):
        print("*"*i)
    else:
        print("*", end="")
        print(" "*(i-2),end="")
        print("*")