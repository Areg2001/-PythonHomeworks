'''իրականացնել map2(func, data1, data2) ֆունկցիա, դրա օգնությամբ գրել ծրագիր, 
որը կտպի էկրանին նոր լիստ, որի i-րդ անդամը կլինի base-ի i-րդ անդամը exp-ի i-րդ 
անդամով աստիճան բարձրացրած, որտեղ base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(base, exp):
    return base ** exp

def map2(func, data1, data2):
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = func(data1[i], data2[i])
        
    return res

print(map2(func, base, exp)) 