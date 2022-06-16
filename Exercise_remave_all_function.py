lst = [1, 5, 4, 9, 58, 4, 3, 4, 58]
def remave_all(data, value):
    i = 0
    while i < len(data):

        if data[i] == value:
            data.remove(value)

        i += 1

    return data

print(remave_all(lst, 58))              
