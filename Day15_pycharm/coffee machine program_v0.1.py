from main import MENU, resources

# 확인차 출력
# print(resources)
# print(MENU["espresso"]["cost"])


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0   # 판매 금액

reduce_water = 0
reduce_milk = 0
reduce_coffee = 0


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




# Turn off the coffee machine by entering "off" to the prompt.
should_continue = False


while not should_continue:


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
        reduce_water = 50
        reduce_milk = 0
        reduce_coffee = 18
        
        # Check resources sufficient?
        if lived_water < 50 or lived_coffee < 18:
            print("Sorry there is not enough ")
        else:
            insert_coins()


    elif user_choice == "latte":
        price = 2.50
        reduce_water = 200
        reduce_milk = 150
        reduce_coffee = 24


        # Check resources sufficient?
        if lived_water < 200 or lived_milk < 150 or lived_coffee < 24:
            print("Sorry there is not enough ")
        else:
            insert_coins()


    elif user_choice == "cappuccino":
        price = 3.00
        reduce_water = 250
        reduce_milk = 100
        reduce_coffee = 24

        # Check resources sufficient?
        if lived_water < 250 or lived_milk < 100 or lived_coffee < 24:
            print("Sorry there is not enough ")
        else:
            insert_coins()


    lived_water = water - reduce_water
    lived_coffee = coffee - reduce_coffee
    lived_milk = milk - reduce_milk


    
# Check resources sufficient?


# Process coins.


# Check transaction succeessful?


# Make Coffee.