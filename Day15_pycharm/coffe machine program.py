from main import MENU, resources

# 확인차 출력
# print(resources)
# print(MENU["espresso"]["cost"])


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def insert_coins():
    print("Please insert coins.")

    quarter = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    quarter_amount = int(input("how many quarters?: "))
    dimes_amount = int(input("how many dimes?: "))
    nickles_amount = int(input("how many nickles?: "))
    pennies_amount = int(input("how many pennies?: "))

    quarter_cost = quarter * quarter_amount
    dimes_cost = dimes * dimes_amount
    nickles_cost = nickles * nickles_amount
    pennies_cost = pennies * pennies_amount

    all_cost = quarter_cost + dimes_cost + nickles_cost + pennies_cost

    if all_cost < price:
        print("Sorry that's not enough money. Money refunded.")
        # money = 0
    if all_cost > price:
        refund_money = all_cost - price
        print(f"Here is ${refund_money} in change.")
        print(f"Here is your {user_choice} ☕. Enjoy!")

# Check resources sufficient?
def resources_sufficient():
    if water < 0 or milk < 0 or coffee < 0:
        print("Sorry there is not enough ")
    else:
        insert_coins()

# Turn off the coffee machine by entering "off" to the prompt.
should_continue = False


while not should_continue:

    money = 0

    # Prompt user by asking "What would you like? (espresso / latte / cappuccino)
    user_choice = input("What would you like? (espresso / latte / cappuccino): ").lower()
    
    if user_choice == "off":
        should_continue = True

    # Print report (Water: ml / Milk: ml / Coffe: g / Money: $)
    elif user_choice == "report":
        print(f"Water: {water} ml")
        print(f"Milk: {milk} ml")
        print(f"Coffee: {coffee} g")
        print(f"Money: $ {money}")

    elif user_choice == "espresso":
        price = 1.50
        water = resources["water"] - 50
        coffee = resources["coffee"] - 18
        resources_sufficient()

    elif user_choice == "latte":
        price = 2.50
        water = resources["water"] - 200
        coffee = resources["coffee"] - 24
        milk = resources["milk"] - 150
        resources_sufficient()

    elif user_choice == "cappuccino":
        price = 3.00
        water = resources["water"] - 250
        coffee = resources["coffee"] - 24
        milk = resources["milk"] - 100
        resources_sufficient()


   


# Check resources sufficient?


# Process coins.


# Check transaction succeessful?


# Make Coffee.