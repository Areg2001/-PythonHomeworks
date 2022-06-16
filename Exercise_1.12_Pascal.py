def Pascal(m, n):
    if n == 1 or m == n:
        return 1

    return Pascal(m - 1, n - 1) + Pascal(m - 1, n)

print(Pascal(5,3))        
