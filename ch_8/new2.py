'''
 Recursion:
    factorial(5)
     /   \
    5 x factorial(4)
         /   \
    5 x 4 x factorial(3)
             /   \
    5 x 4 x 3 x factorial(2)
                 /   \
    5 x 4 x 3 x 2 x facorial(1)
                     /
    5 x 4 x 3 x 2 x 1

'''

def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

n=int(input("Enter a number :"))
print(f"the factorial of this number is : {fact(n)}")
