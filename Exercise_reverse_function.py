lst = [1, 8, 4, 56, 4, 14, 57, 36]

def reverse_(data):
    i = 0
    while i < len(data)/2:
       data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
       i+=1
       
    return data

print(reverse_(lst))        