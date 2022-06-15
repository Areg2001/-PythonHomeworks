def sum_inside_numbers(a, b):
    i = a
    sum = 0

    while  i <= b:
       sum += i
       i += 1

    return sum

print(sum_inside_numbers(3, 8))        
