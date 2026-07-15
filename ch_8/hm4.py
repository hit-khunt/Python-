l = ["hit","samir","het","suresh","harry","sanjay","hitesh","suhan"]

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(rem(l, "hit"))