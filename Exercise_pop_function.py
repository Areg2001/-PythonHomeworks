lst = [3,4,5,6]

def pop_(data, index):

    if index == None:
        del data[-1]
        return data

    tmp = data[index]
    del data[index]
    return tmp

print(pop_(lst, 2)) 
print(lst)     
        

