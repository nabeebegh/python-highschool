def addspace(x):
    k = 0
    length = len(x)
    currentstring = ""
    while k < length:
        currentstring = str(x[k]) + " " + currentstring
        k = k + 1
    print(currentstring)
    
