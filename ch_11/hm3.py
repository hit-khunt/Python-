class Complex:
    def __init__(c1, r, i):
        c1.i = i
        c1.r = r

    def __add__(c1, c2):
        return Complex(c1.r + c2.r, c1.i + c2.i) 

    def __mul__(c1, c2):
        real_part = c1.r*c2.r - c1.i*c2.i
        imag_part = c1.r*c2.i - c1.i*c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1,2)
c2 = Complex(2,3)
print(c1 + c2)
print(c1*c2)