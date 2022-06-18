''' Իրականացնել map  ֆունկցին, որի միջոցով գրել triple(data) ֆունկցիա,
որը վերադարձնում է data-ի անդամների եռապատիկները պարունակող լիստ:'''
lst = [2, 4, 7, 25, 3, 5, 6]
def triple(data):
    return data * 3
    
def map_(triple, data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = triple(data[i])
        
    return res
    
print(map_(triple, lst))