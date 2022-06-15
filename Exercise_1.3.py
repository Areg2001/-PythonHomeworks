def Pow(a):
    return a ** 2

def two_biggest_numbers_square_sum(a,b,c):
    return Pow(a) + Pow(b) + Pow(c) - Pow(min(a,b,c))

print(two_biggest_numbers_square_sum(10, 8, 7))    
    