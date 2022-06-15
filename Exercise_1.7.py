def zero_degree_of_number(a,b):
    return 1

def degree_of_number(a, b):
    return a ** b

def degree_of_reversal(a, b):
    return ((1/a) ** (-b))

def pow(a, b):
    if(b > 0):
       return degree_of_number(a, b)
    elif(b < 0):
        return degree_of_reversal(a,b)
    elif(b == 0):
        return zero_degree_of_number(a,b)        

print(pow(2,0))            

"""We do not need to chek a == 0 and b < 0 case because Python
   will automatically give an ZeroDivisionError"""

