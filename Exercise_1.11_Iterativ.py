
def f(n):

    if(n < 3):
        return n

    first,second,third,nextItem,counter = 0, 1, 2, 0 , 3

    while counter <= n:
        nextItem = first + second + third
        first,second,third = second, third, nextItem
        counter += 1

    return nextItem    

print(f(21))  


