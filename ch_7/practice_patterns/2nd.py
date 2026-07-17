n = int(input("Enter a even number :"))

for i in range(1,n+1):
    if(i<=n/2):
        print("*"*i, end="")
        print(" "*(n-(2*i)), end="")
        print("*"*i)
    else:
        print("*"*(n-i+1), end="")
        print(" "*((2*i)-n-2), end="")
        print("*"*(n-i+1))

# n = int(input("Enter an even number: "))

# for i in range(1, n + 1):
#     if i <= n // 2:
#         stars = i
#     else:
#         stars = n - i + 1

#     spaces = n - 2 * stars
#     print("*" * stars + " " * spaces + "*" * stars)