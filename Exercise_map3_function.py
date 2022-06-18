'''Իրականացնել map3(func, data1, data2, data3) ֆունկցիա, որը վերադարձնում է նոր լիստ, 
որի մեջ ներառված են func-ի կանչի արդյունքները data1, data2 և data3-ի համապատասխան անդամների վրա, 
օրինակ,եթե ունենք sum(a, b, c) ֆունկցիան, որը վերադարձնում է a, b և c թվերի գումարը, 
map(sum, [1, 2, 3], [10, 20, 30], [100, 200, 300]) կվերադարձնի [111, 222, 333]:'''

lst1 = [5, 6, 8, 9, 3]
lst2 = [4, 8, 3, 1, 10]
lst3 = [7, 6, 9, 8, 9]

def func(data1, data2, data3):
    return data1 + data2 + data3
        
def map3(func, data1, data2, data3):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = func(data1[i], data2[i], data3[i])
    
    return res
    
print(map3(func, lst1, lst2, lst3))    