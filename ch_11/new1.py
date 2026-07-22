# multiple inheritance

class Employee:
    company = "ITC"
    salary = 120000
    def show(self):
        print(f"The name of the the employee is {self.company} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all language here is your language : {self.language}")

class Programmer(Employee, Coder):
    company = "ITC InfoTech"
    def showlanguage(self):
        print (f"The name is {self.company} and he is good with {self.language} language.")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showlanguage()