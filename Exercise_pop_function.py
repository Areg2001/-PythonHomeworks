lst = [3,4,5,6]

def pop_(data, index):

    if index == None:
        tmp = data[-1]
        del data[-1]
        return tmp

    tmp = data[index]
    del data[index]
    return tmp

print(pop_(lst, 2)) 
print(lst)     
        

