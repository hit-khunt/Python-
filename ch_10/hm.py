class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Hit", 120000, 395010)
print(p.name, p.salary, p.pin, p.company)

p = Programmer("Het", 100000, 360005)
print(p.name, p.salary, p.pin, p.company)