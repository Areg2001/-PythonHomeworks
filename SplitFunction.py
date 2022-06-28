def SplitFunction(source, sep, count):
    str, lst, j = '', [], 0
    for i in range(len(source)):
        str += source[i]
        if source[i] == sep and j < count:
            str = str.replace(sep, '')
            lst.append(str)
            str = ''
            j += 1
    lst.append(str)        
    return lst    

print(SplitFunction('H,ello Wor,ld,!', ',', 1))            

