# multi-level inheritance

class Employee:
    a = 2

class Programmer(Employee):
    b = 3

class Manager(Programmer):
    c = 4

o = Manager()
print(o.b)

# Manger
#   |
# Programmer
#   |
# Employee