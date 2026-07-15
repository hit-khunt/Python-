#   *
#  ***
# *****

n = int(input("Enter the number :"))

for i in range(1,n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1))
#print by default adds new line
# by using end="" we can stop that