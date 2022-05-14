#Escopo Local

def test(b):
    a = 9
    b += 7
    print(b)

a = 7
test(a)
print(a)

#Escopo Global

def test2(b):
    global a
    a = 9
    b += 7
    print(b)

test2(a)
print(a)