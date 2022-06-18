lst = [2, 4, 4, 25, 3, 5, 6]
def triple(data):
    return data * 3
    
def map_(triple, data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = triple(data[i])
        
    return res
    
print(map_(triple, lst))