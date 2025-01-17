import random

menu = {
    "HF01": {"name": "Cup Noodles", "price": 10.00, "stock": 11, "category": "Hot Food"},
    "HF02": {"name": "Hot Pockets", "price": 15.00, "stock": 9, "category": "Hot Food"},
    "S01": {"name": "Chips", "price": 5.00, "stock": 4, "category": "Snacks"},
    "S02": {"name": "Croissant", "price": 2.50, "stock": 10, "category": "Snacks"},
    "S03": {"name": "Chocolate", "price": 1.99, "stock": 15, "category": "Snacks"},
    "CD01": {"name": "Orange Juice", "price": 3.50, "stock": 7, "category": "Cold Drinks"},
    "CD02": {"name": "Iced Americano", "price": 5.00, "stock": 5, "category": "Cold Drinks"},
    "CD03": {"name": "Soda", "price": 5.00, "stock": 14, "category": "Cold Drinks"},
    "HD01": {"name": "Karak Tea", "price": 1.00, "stock": 3, "category": "Hot Drinks"}
}

def menu_list(): # this is where the menu will be displayed
    print("╭────────────────────────────────────────────────────.★..─╮\n\n" +
"""\t╭───────────────────༺♡༻──────────────────╮
\t   Welcome to Hamartia Vending Machine!
\t╰────────────────────────────────────────╯\n\n""")
    menu_title = "⋆ ˚｡⋆୨ ʚ MENU ɞ ୧⋆ ˚｡⋆"
    print(f'{menu_title:^55}') # centered format of the menu display
    print("     ╭ \t\t\t\t\t\t    ╮")
    for code, product in menu.items():
        print(f"\t{code}: {product['name']:^14} - £{product['price']:.2f} ({product['stock']} in stock)") 
    print("     ╰ \t\t\t\t\t\t    ╯")
    print("\n")
    
# a way of managing the money so the user can input any amount of money and have the correct change returned
def ask_payment(user_choice):
    user_payment = 0
    product = menu[user_choice]
    price = product["price"]
    if user_payment != price:
        bill = float(input("Please insert the correct amount in coins or notes: £"))
        user_payment += bill
    return user_payment
        
# an intelligence system for suggesting purchases
def suggest_product(last_purchase):
    if last_purchase["category"] == "Hot Drinks" or last_purchase["category"] == "Cold Drinks":
        suggestions = ["S01", "S02", "S03"] # if the product purchased is a drink then the machine will suggest a snack
    elif last_purchase["category"] == "Snacks":
        suggestions = ["CD01", "CD02", "CD03", "HD01"] # if the product purchased is a snack then the machine will suggest a drink
    else:
        suggestions = ["CD01", "CD03"] # if the product purchased is a hot food then the machine will suggest a cold drink
    return random.choice(suggestions) # randomizes the selection of suggestions within a certain category of products
        
def dispense_product(user_choice):
    product = menu[user_choice]
    name = product["name"]
    if product["stock"] > 0:
        product["stock"] -= 1 # the product stock will be reduced by 1 whenever the user purchases it
        print(f"\nDispensing {name}...")
        print(f"{name} dispensed.") # a message that tells the user that a particular drink or snack has been dispensed
        print("\nThank you for using Hamartia Vending Machine!\n")
    else:
        print("Sorry, this product is out of stock.") # a message that tells the user that a product is out of stock
        print("\nThank you for using Hamartia Vending Machine!\n")
        
def short_payment(user_payment, price):
    short_amount = price - user_payment
    while user_payment < price:
        print(f"You are £{short_amount} short.") # a message that tells the user how much money they need to add if they paid short
        remaining_amt = float(input("Please pay the remaining amount: £"))
        user_payment += remaining_amt

def return_change(user_payment, price):
    change = user_payment - price
    if change > 0:
        print(f"Your change is £{change:.2f}.") # a message that tells the user how much change they have received

def main():
    last_purchase = None # the last_purchase determines what product will be suggested after purchasing
    while True: #ensures that the code will not finish unless the user will input 'q' 
        menu_list()
        user_choice = input("Enter product code (or 'Q' to quit): ") # a way of allowing users to buy additional items; the code will not finish executing unless the user types 'q'
        if user_choice.lower() == 'q':
            print("\n╰─..★.────────────────────────────────────────────────────╯") # prints if the user inputs 'q' to break the code
            break
        
        product = menu.get(user_choice)
        
        if product:
            if product["stock"] > 0:
                user_payment = ask_payment(user_choice)
                short_payment(user_payment, product["price"])
                return_change(user_payment, product["price"])
                dispense_product(user_choice)
                last_purchase = product
                suggestion = suggest_product(last_purchase)
                print(f"Consider buying {menu[suggestion]["name"]} for your next purchase.\n")
                print("╰─..★.────────────────────────────────────────────────────╯")
            else:
                print("Sorry, this product is out of stock.\n")
                print("╰─..★.────────────────────────────────────────────────────╯")
        else:
            print("Invalid product code.\n\n" + 
                  "╰─..★.────────────────────────────────────────────────────╯") # prints if the user inputs the wrong product code
        
    
if __name__ == "__main__":
    main()