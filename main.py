# project coffee machine
# has three flavors
# 1 espresso contains
# 50ml water and 18g coffee
# 2 Latte
# 200ml water and 24g coffee 150ml milk
# 3 Cappuccino
# 250ml water and 24g coffee 100ml milk

# coin operated using : penny 1, dime 10, nickle 5, and quarter 25
# print report

def insertion(money_debt):
    status1 = True
    print("Insert coins")
    quarter = int(input("How many quarters? ")) * 0.25
    nickle = int(input("How many nickles? ")) * 0.10
    dime = int(input("How many dimes? ")) * 0.05
    pennie = int(input("How many pennies? ")) * 0.01
    total_insertion = quarter + nickle + dime + pennie
    value = total_insertion - money_debt
    if value > 0:
        print(f"Thank you for your payment. here is your change {value}$")
    elif value == 0:
        print("Thank you for your payment")
    else:
        print("Sorry that's not enough money. Money refunded")
        status1 = False
    return status1
should_continue = True
water = 300
milk = 200
coffee = 100
money = 0
def check_remaining(water_re, coffee_re, milk_re):
    status = True
    if type == "latte" and water_re < 200:
        print("Sorry there is not enough water")
        status = False
    elif type == "latte" and coffee_re < 24:
        print("Sorry there is not enough coffee")
        status = False
    elif type == "latte" and milk_re < 150:
        print("Sorry there is not enough milk")
        status = False
    elif type == "espresso" and water_re < 50:
        print("Sorry there is not enough water")
        status = False
    elif type == "espresso" and coffee_re < 18:
        print("Sorry there is not enough coffee")
        status = False
    elif type == "cappuccino" and water_re < 250:
        print("Sorry there is not enough water")
        status = False
    elif type == "cappuccino" and coffee_re < 24:
        print("Sorry there is not enough coffee")
        status = False
    elif type == "latte" and milk_re < 100:
        print("Sorry there is not enough milk")
        status = False

    return status

while should_continue:

    type = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if type == "espresso":
        if check_remaining(water, coffee, milk):
            water -= 50
            coffee -= 18
            money += 1.50
            insertion(money)
            print("Her is your espresso!")
    elif type == "latte":
        if check_remaining(water, coffee, milk):
            water -= 200
            coffee -= 24
            milk -= 150
            money += 2.50
            insertion(money)
            print("Her is your latte!")
    elif type == "cappuccino":
        if check_remaining(water, coffee, milk):
            water -= 250
            coffee -= 24
            milk -= 100
            money += 2.50
            insertion(money)
            print("Her is your cappuccino!")
    elif type == "off":
        should_continue = False
    elif type == "report":
        print(f"Water: {water}ml\n Milk: {milk}ml\n Coffee: {coffee}g\n Money: {money}$")
    else:
        print("Invalid Entry")

# order()
