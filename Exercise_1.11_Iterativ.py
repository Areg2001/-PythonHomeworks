
def f(n):

    if(n in (1, 2, 3)):
        return n

    first,second,third,nextItem,counter = 1, 2, 3, 0 , 1

    while counter <= n - 3:
        nextItem = first + second + third
        first,second,third = second, third, nextItem
        counter += 1

    return nextItem    

print(f(7))  


