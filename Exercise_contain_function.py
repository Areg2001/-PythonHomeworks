lst = [1, 2, 3, 4, 8, 7, 9, 2]
def contain_(data, val):
    i = 0
    while i < len(data):

        if data[i] == val:
            return True

        i+= 1

    return False        
            
print(contain_(lst, 2))            

