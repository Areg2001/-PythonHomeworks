def sum_inside_numbers(a, b):
    if a > b:
        a, b = b, a

    sum, i = 0, a    

    while i <= b:
        sum += i
        i += 1

    return sum

print(sum_inside_numbers(4 , 8))            