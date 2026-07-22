class Employee:
    salary = 434
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100)) 

    @salaryAfterIncrement.setter  
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 600
print(e.increment)