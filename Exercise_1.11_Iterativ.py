

def f(n):

    if(n in (1, 2, 3)):
        return n

    first,second,third, nexterm,counter = 1, 2, 3, 0 , 1

    while counter <= n - 3:
        nexterm = first + second + third
        first = second
        second = third
        third = nexterm
        counter += 1

    return nexterm    


print(f(7))        



