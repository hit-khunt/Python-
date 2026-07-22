class Employee:
    a = 2
    # def show(self):
    #     print(self.a) it prints 45

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.fname

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45
e.name = "Hit Khunt"
print(e.fname, e.lname)

e.show()