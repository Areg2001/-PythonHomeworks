def f(n):
    return n if n < 3 else f(n-1) + f(n-2) + f(n - 3)

print (f(5))    