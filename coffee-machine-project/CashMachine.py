class CashMachine:
    def __init__(self):
        print("Please insert coins")
        self.q = int(input("How many Quaters ?: "))
        self.d = int(input("How many Dimes ?: "))
        self.n = int(input("How many Nickels ?: "))
        self.p = int(input("How many Pennies ?: "))

    def get_dollars(self):
        dollars = ((self.q*25)+(self.d*10)+(self.n*5)+(self.p))/100
        return dollars
