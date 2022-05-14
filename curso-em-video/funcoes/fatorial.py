def fatorial(n, show = False):
    aux = 1
    for x in range(n, 0, -1):
        aux *= x
        if show:
            print(x,end='')
            if x > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
    return aux

print('-'*10)
print(fatorial(4, True))
print('-'*10)
print(fatorial(4, False))