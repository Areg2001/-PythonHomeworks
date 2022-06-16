lst = [1, 3, 9, 87, 4, 5, 12]
def pop_(i):
    value = 0
    if i == None:
        del lst[len(lst) - 1]
    else:
        value = lst[i]
        del lst[i]
        return value
        

print(pop_(5))
print(lst)
      


    
        
        
    
