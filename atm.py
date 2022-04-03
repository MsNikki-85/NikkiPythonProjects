def main():

    #we are using two-dimensional lists to store the balance of multiple users   
    balance = [["JOHN",5000],
               ["JANE",5000],
               ["JOE", 5000]]

    #the following 3 functions are defined inside of the main() function
    #which means their scope is limited within the main()
    def convert(currency, amount):
        if (currency == "USD"):
            return amount
        elif (currency == "EUR"):
            amount = amount / 0.86
            return int(amount)
        elif (currency == "CAD"):
            amount = amount / 1.3
            return int(amount)

    def updateBalance(name, amount):
        for account in balance:
            if (account[0] == name):
                account[1] = account[1] + amount

    def getBalance(name):
        for account in balance:
            if (account[0] == name):
                return account[1]

    name = input("Please enter your name: ").upper()
    transaction = input("Please enter deposit or withdraw: ").upper()

    if (transaction == "DEPOSIT"):
        currency = input("Please enter the currency. It can be USD, EUR, or CAD:").upper()       
        amount = int(input("Please enter the amount you'd like to deposit:"))         
        print (name, ", you are depositing "+currency, amount)

        amount_in_usd = convert (currency,amount)
        updateBalance(name, amount_in_usd)
        
    elif (transaction == "WITHDRAW"):
        currency = input("Please enter the currency. It can be USD, EUR, or CAD:").upper()
        amount = int(input("Please enter the amount you'd like to withdraw:"))
        print (name, ", you are withdrawing "+currency, amount)

        amount_in_usd = convert (currency,amount)
        updateBalance(name, 0-amount_in_usd)
    else:
        print ("The input is not valid.")

    print (name, ", your remaining balance is: ", getBalance(name))

main()
