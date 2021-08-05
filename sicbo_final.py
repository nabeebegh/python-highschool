import random
random.seed()
global balance
balance = 0

def printChoices():
    global balance
    print("1. BET on LARGER.")
    print("2. BET on SMALLER.")
    print("3. BET on EQUAL.")
    print("4. Cash out with current balance of $" + str(balance))
    userChoice = input("Your choice: ")
    return(userChoice)
    
def rollDice():
    global balance
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    rollDice = dice1,dice2,dice3
    print("")
    print("Dealer rolled " + str(rollDice) + " with the sum of " + str(sum(rollDice)) + ".")
    return(rollDice)

def sicbo():
    print('')
    print("---------------Welcome to Sic-bo!-----------------")
    global balance # balance (global variable)
    currentRoll = rollDice()# first roll
    userChoice = printChoices()
    while userChoice != "1" and userChoice != "2" and userChoice != "3" and userChoice != "4":
        print('')
        print("Invalid input.")
        print('')
        userChoice = printChoices()
    newRoll = rollDice() #second roll
    if (userChoice == "1") and (sum(newRoll) > sum(currentRoll)):
        print("You win $1.")
        balance += 1
        print("Balance: $" + str(balance))
        sicbo() # repeat function
    elif (userChoice == "2") and (sum(newRoll) < sum(currentRoll)):
        print("You win $1.")
        balance += 1
        print("Balance: $" + str(balance))
        sicbo() # repeat function
    elif (userChoice == "3") and (sum(newRoll) == sum(currentRoll)):
        print("Congratulations, you win $5!")
        balance += 5
        print("Balance: $" + str(balance))
        sicbo() # repeat function
    elif (userChoice == "4"):
        print("Cashed out $" + str(balance) + "." + " See you again!")
        print('')
        print("--------------------GAME END----------------------")
        return(None)
    else:
        print("You lose all your money.")
        balance = 0
        print("Balance: " + str(balance))
        sicbo() # repeat function

