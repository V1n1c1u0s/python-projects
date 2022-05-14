def contador(*num):
    print(num, end=' ')
    s = 0
    for x in num:
        s += x
    print(s)

contador(5,5)
contador(7,8,1)
contador(9,9,8,1)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [0,1,2,3,4,5,6]
dobra(valores)
print(valores)