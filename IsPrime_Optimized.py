import time
def isPrime2(n):
        if type(n) == str or type(n) == float or (n < 0):
            return("Please enter positive integers only")
        startTime = time.time()
        k = 0
        if n % 2 == 0:
            k = n - 1
        else:
            k = n - 2
        result = True
        while (result == True) and (k >= 2):
            if (n % k == 0):
                result = False
            k -= 2
        endTime = time.time()
        print(endTime - startTime)
        return(result)
