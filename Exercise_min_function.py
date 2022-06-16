lst = [15, 0,25, 9, -7 ,7, 5]

def min_(data):
    i = 0
    while i < len(data) - 1:
        if data[i] < data[i+1]:
             data[i], data[i+1] = data[i+1], data[i]
             
        i += 1

    return data[len(data) - 1]

print(min_(lst))            