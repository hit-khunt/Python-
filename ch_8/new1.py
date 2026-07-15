# def gd():
#     name=input("Enter your name :")
#     print("good day,",name)

# gd()

# def gd(name, ending):
#     print("good day,",name)
#     print(ending)

# gd("Hit", "Thank you")
# gd("Het", "Thanks")

def gd(name):
    print("good day,",name)
    return "done"

a = gd("Hit")
print(a)
# if return is not given then a will give none
# it does not return anything(None)

def gd(name, ending="Thank you"):
    print("good day,",name)
    print(ending)

gd("Hit")
gd("Het", "Thanks")
