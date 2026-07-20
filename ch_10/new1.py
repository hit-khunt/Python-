class employee:
    language = "Python"
    salary = 140000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning.")

hit = employee()
hit.greet()
hit.getinfo() # same thing employee.getinfo(hit)