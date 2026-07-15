# * * *
# *   *  for n=3
# * * *
n = int(input("Enter the number :"))

i=1
while(i<n+1):
    if(i==1 or i==n):
        print("* "*n)
    else:
        print("*", end="")
        print(" "* (2*n-3), end="")
        print("*")
    i+=1
    