class Employee:
    language = "Python"
    salary  = 120000

    def __init__(self, name, language, salary): # Dunder method which is automatically called when object created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("good morning")

hit = Employee("Hit", "Java", 1200000)
hit.greet()
# hit.name = "Hit"
print(hit.name, hit.salary, hit.language)

