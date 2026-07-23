
a = int(input("Enter a number : "))
b = int(input("Enter second number : "))

if(b==0):
    raise ZeroDivisionError("Number can't divide by zero.")
else:
    print(f"The division a/b is {a/b}")
