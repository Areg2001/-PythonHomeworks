s = 'aaaaassdaaadfaafgg'
def ReplaceFunction(source, old, new, count):
    res = ''
    i = 0
    while i < len(s):
        if source[i:i+len(old)] == old and count > 0:
            res += new
            count -= 1
            i += len(old)
        else:
            res += source[i]
            i += 1
    return res
print(ReplaceFunction(s, 'aa', 'b',4))    
