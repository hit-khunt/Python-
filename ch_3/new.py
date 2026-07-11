greeting = "good morning, "
name = "Hit khunt"
a = greeting + name 
print(a)
# string  H  i  t  _  k  h  u  n  t 
#        /  /  /  /  /  /  /  /  /
#       0  1  2  3  4  5  6  7  8   like arrey but also../
#      -9 -8 -7 -6 -5 -4 -3 -2 -1         <-------------/
print(name[0])
print(name[1])
print(name[2])
# name[1] = "k" --> Does not work

print(name[2:6])
#        ^ 
#        |
# it gives 2 to 5 charaters

b = name[0::2]
print(b)