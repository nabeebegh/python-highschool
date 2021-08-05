def reverse(myString):
    try:
        length = len(myString)
        k = len(myString) - 1
        reverse = "" 
        while k < length and k != -1:
            reverse = reverse + str(myString[k])
            k -= 1
        print(reverse)
    except:
        print("Invalid Entry")
