def is_even(n):
    return n % 2 == 0

def square(m, n):
    return m ** n


def fast_pow(m, n):
    res, count = 0, 0

    while count <= abs(n):
        if is_even(n):
            res = square(m, n/2) ** 2
        else:
            res = m * square(m, n - 1)
   
        count+= 1  
    return res      

print(fast_pow(5, -2))                
