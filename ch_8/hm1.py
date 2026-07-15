def f2c(f):
    return 5*(f-32)/9

f = int(input("Enter tempreture in fahrenheit :"))
c = f2c(f)
print(f"{round(c,2)}°C")