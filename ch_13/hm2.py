a = [1, 5, 23, 12, 454, 15, 30, 45, 56]

def greatest():
    largest = a[0]

    for i in a:
        if i > largest:
            largest = i

    return largest

print(greatest())
            
