import random
random.seed()


def sicbo():

    money = 0
    print("You have $" + str(money))
        
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    dSum1 = d1+d2+d3

    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1)) 
    print("1. Bet on LARGER.")
    print("2. Bet on SMALLER.")
    print("3. Bet on EQUAL.")
    print("4. Quit.")

    decision = input("Your choice: ")
            
    while decision != "4":
    
            if decision == "1":
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                d3 = random.randint(1,6)
                dRolled = (d1, d2, d3)
                dSum = d1+d2+d3
                if dSum > dSum1:
                    money = money + 1
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum))
                    print("You win $1")

                    print("-----------------------------------------------------------")
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    dSum1 = d1+d2+d3
                    print("You have $" + str(money))
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1))
                    print("1. Bet on LARGER.")
                    print("2. Bet on SMALLER.")
                    print("3. Bet on EQUAL.")
                    print("4. Quit.")

                    decision = input("Your choice: ")
                else:
                    money = 0
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum))
                    print("You lose all your money")

                    print("-----------------------------------------------------------")
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    dSum1 = d1+d2+d3
                    print("You have $" + str(money))
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1)) 
                    print("1. Bet on LARGER.")
                    print("2. Bet on SMALLER.")
                    print("3. Bet on EQUAL.")
                    print("4. Quit.")

                    decision = input("Your choice: ")

                    
            elif decision == "2":
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                d3 = random.randint(1,6)
                dRolled = (d1, d2, d3)
                dSum = d1+d2+d3
                if dSum < dSum1:
                    money = money + 1
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum))
                    print("You win $1")

                    print("-----------------------------------------------------------")
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    dSum1 = d1+d2+d3
                    print("You have $" + str(money))
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1)) 
                    print("1. Bet on LARGER.")
                    print("2. Bet on SMALLER.")
                    print("3. Bet on EQUAL.")
                    print("4. Quit.")

                    decision = input("Your choice: ")
                else:
                    money = 0
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum))
                    print("You lose all your money")

                    print("-----------------------------------------------------------")
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    dSum1 = d1+d2+d3
                    print("You have $" + str(money))
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1)) 
                    print("1. Bet on LARGER.")
                    print("2. Bet on SMALLER.")
                    print("3. Bet on EQUAL.")
                    print("4. Quit.")

                    decision = input("Your choice: ")

                    
            elif decision == "3":
                
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                d3 = random.randint(1,6)
                dSum = d1+d2+d3
                if dSum == dSum1:
                    money = money + 5
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum))
                    print("You win $5")

                    print("-----------------------------------------------------------")
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    dSum1 = d1+d2+d3
                    print("You have $" + str(money))
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1)) 
                    print("1. Bet on LARGER.")
                    print("2. Bet on SMALLER.")
                    print("3. Bet on EQUAL.")
                    print("4. Quit.")

                    decision = input("Your choice: ")
                else:
                    money = 0
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum))
                    print("You lose all your money")

                    print("-----------------------------------------------------------")
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    d3 = random.randint(1,6)
                    dSum1 = d1+d2+d3
                    print("You have $" + str(money))
                    print("Dealer Rolled " + "(" + str(d1) + "," + str(d2) + "," + str(d3) + ")" + " with a sum of " + str(dSum1)) 
                    print("1. Bet on LARGER.")
                    print("2. Bet on SMALLER.")
                    print("3. Bet on EQUAL.")
                    print("4. Quit.")

                    decision = input("Your choice: ")

                    
            elif decision != "1" or decision != "2" or decision != "3" or decision != "4":
                print("-----------------------------------------------------------")
                print("Please pick one of the numbers from the list above that corresponds with your choice.")
                decision = input("Your choice: ")
                

    if decision == "4":
            print("Take your money: $" + str(money) + ". Good bye.")
            return(None)
            
            
                
                
            
            
            

        

