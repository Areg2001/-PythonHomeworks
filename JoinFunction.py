def JoinFunction(data, sep):
    newString = ''
    for i in range(len(data)):
        newString += data[i] + sep
        
    return newString

print(JoinFunction(['sadsad', 'xzcas', 'jhkjhk'], '; '))        