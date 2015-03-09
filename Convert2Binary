def convertToBinary(n):
        try:
                currentstring = ""
                if n == 0:
                    return(0)
        
                currentstring = ""

                if n < 0:
                        n = n * -1
                        while n > 0:
                         r = n%2
                         n = n//2
                         currentstring = str(r) + currentstring
                        return(int(currentstring)*-1)
                        
        
                while n > 0:
                    r = n%2
                    n = n//2
                    currentstring = str(r) + currentstring
                return(int(currentstring))


        except:
                if type(n) == float:
                        print("Error, invalid entry. (float)")
                elif type(n) == str:
                        print("Error, invalid entry. (string)")
