m1 = int(input("Enter the marks of Maths :"))
m2 = int(input("Enter the marks of Pysics :"))
m3 = int(input("Enter the marks of Chemistry :"))

a1 = m1*100/80
a2 = m2*100/80
a3 = m3*100/80

print("your persentage of maths is :",a1)
print("your persentage of pysics is :",a2)
print("your persentage of Chemistry is :",a3)

finalm = (a1+a2+a3)/3

if(a1<33):
    print("you are fail in Maths.")
else:
    print("you are pass in maths.")

if(a2<33):
    print("you are fail in Pysics.")
else:
    print("you are pass in Pysics.")

if(a3<33):
    print("you are fail in Chemistry.")
else:
    print("you are pass in Chemistry.")

print("Allover persentage :",finalm)

if(finalm>=40 and a1>33 and a2>33 and a3>33):
    print("you are passed. Congratulations!")
else:
    print("you are failed. try again next year")