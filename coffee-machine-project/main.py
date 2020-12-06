from MenuItem import MenuItem
from CoffeeMachine import CoffeeMachine

loop = 'yes'
cm = CoffeeMachine()
while loop == 'yes':
    inp = input("What would you like ? (espresso/latte/cappuccino) : ")
    if(inp == "report"):
        cm.display_resources()
    else:
        item = MenuItem(inp)
        enough = cm.check_resources(item)
        if(enough == True):
            cm.get_drink(item)
        loop = input("\nWould you like an another drink ? 'yes' or 'no' : ")
