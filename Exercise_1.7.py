def pow(a, b):
    res,count = 1, 0

    if b < 0:
        a = 1/a

    while count < abs(b):
        res = res * a
        count = count + 1

    return res       

print(pow(4,-3))            

"""We do not need to check a == 0 and b < 0 case because Python
   will automatically give an ZeroDivisionError"""

