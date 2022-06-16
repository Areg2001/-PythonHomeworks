def double(n):
    return n * 2

def halve(n):
    if n % 2 == 0:
        return n / 2

def fast_mul(a,b):

    if a == 0 or b == 0:
        return 0

    if(halve(b)):
        return double(fast_mul(a, halve(b)))
    else:
        return a + fast_mul(a, b-1)

print(fast_mul(0,3))                     
