lst = [105, 0,25, 9, -7 ,7, 57]

def max_(data):
    i = 0
    while i < len(data) - 1:
        if data[i] > data[i+1]:
             data[i], data[i+1] = data[i+1], data[i]
             
        i += 1

    return data[len(data) - 1]

print(max_(lst))            