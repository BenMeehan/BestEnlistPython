from CashMachine import CashMachine


class CoffeeMachine:
    resources = {
        "Milk": 200,
        "Water": 300,
        "Coffee": 100
    }
    money = 0
    dollars = 0
    change = 0

    def display_resources(self):
        keys = self.resources.keys()
        for i in keys:
            if i == 'Coffee':
                print(f"{i}: {self.resources[i]}g")
                continue
            print(f"{i}: {self.resources[i]}ml")
        print(f"Money: ${self.money}")

    def check_resources(self, drink):
        if(drink.name != 'espresso' and self.resources['Milk'] < drink.milk):
            print("Sorry there is not enough milk.")
            return False
        elif(self.resources['Water'] < drink.water):
            print("Sorry there is not enough water.")
            return False
        elif(self.resources['Coffee'] < drink.coffee):
            print("Sorry there is not enough coffee.")
            return False
        else:
            if(drink.name != 'espresso'):
                self.resources['Milk'] -= drink.milk
            self.resources['Water'] -= drink.water
            self.resources['Coffee'] -= drink.coffee
            return True

    def get_drink(self, item):
        cash_machine = CashMachine()
        self.dollars = cash_machine.get_dollars()
        if(self.dollars < item.cost):
            print("Sorry thats not enough money. Money refunded.")
        else:
            self.money += item.cost
            self.change = self.dollars-item.cost
            print(f"Here is ${self.change} in change.")
            print(f"Here is your {item.name} enjoy!")
