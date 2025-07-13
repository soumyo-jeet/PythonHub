import menu_chart

resources = {
    "water" : 100,
    "milk" : 150,
    "coffee" : 50
}

def report():
    print(f'''
    Water : {resources["water"]} ml
    Milk : {resources["milk"]} ml
    Coffee : {resources["coffee"]} gm
    ''')

def resource_checking(water, milk, coffee):
    if resources["coffee"] >= coffee and resources["milk"] >= milk and resources["water"] >= water:
        return True
    elif resources["coffee"] < coffee:
        return "Coffee is not available! Sorry!"
    elif  resources["milk"] < milk:
        return "Milk is not available! Sorry!"
    else:
        return  "Water is not available! Sorry!"

def cash_counter(price, quaters, dimes, pennies):
    total_insterted = quaters * 0.25 + dimes * 0.10 + pennies * 0.01
    balance= total_insterted - price
    return balance 

def make_order(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


finish = False   
while not finish:
    command = input("What do you want? (capitune, latte, dark): ").lower()
    if command in ['capitune', 'latte', 'dark'] :
        selected_coffee = menu_chart.requirments[command]
        water = selected_coffee["water"]
        milk= selected_coffee["milk"]
        coffee = selected_coffee["coffee"]
        price= selected_coffee["price"]

        print("Resource availablity is checking...")
        proceed = resource_checking(water, milk, coffee)

        if proceed == True:
            print(f"Please pay {price}.\nInsert Coins: ")
            quaters = int(input("quaters= "))
            dimes = int(input("dimes= "))
            pennies = int(input("pennies= "))
            balance = cash_counter(price, quaters, dimes, pennies)

            if balance >= 0:
                print(f"I am preparing your order. Here is your change {round(balance , 2)}")
                make_order(water, milk, coffee)
                print("Your Order is ready! Get it!!")
            else:
                print("Not sufficient coins! Your payment is refunded!")
                
        else:
            print(proceed)

    elif command == 'report':
        report() 
 
    elif command == 'off':
        print("\n" * 100)
        finish = True

    else:
        print("Invalid entre!")













