for i in range(5):
    pass
# pass while bypass the code to next 
# when we use pass in any code we can update that letter
# it will not give us error even if code is incomplet

for i in range(101):
    if(i==67):
        break #break Exits(break) the loop 
    print(i)

# this code will print 0 to 101 numbers with skiping evvery 5th number 
for i in range(101):
    if(i in range(0,101,5)):
        continue #implement for next value skip the given one
    print(i)