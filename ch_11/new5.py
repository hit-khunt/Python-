class Number:
    def __init__(self, n):
        self.n=n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n+m)

# for + p1.__add__(p2)
# - __sub__
# * __mul__ 
# / __truediv__
# // __floordiv__