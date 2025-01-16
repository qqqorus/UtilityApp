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

def menu_list():
    print("MENU")
    for code, product in menu.items():
        print(f"{code}: {product['name']} - £{product['price']:.2f} ({product['stock']} in stock)")
    print("\n")
    
def ask_payment(user_choice):
    user_payment = 0
    product = menu[user_choice]
    price = product["price"]
    if user_payment != price:
        bill = float(input("Please insert the correct amount in coins or notes: £"))
        user_payment += bill
    return user_payment
        
def dispense_product(user_choice):
    product = menu[user_choice]
    name = product["name"]
    if product["stock"] > 0:
        product["stock"] -= 1 
        print(f"\nDispensing {name}...")
        print(f"{name} dispensed.") 
        print("\nThank you for using Hamartia Vending Machine!\n")
    else:
        print("Sorry, this product is out of stock.") 
        print("\nThank you for using Hamartia Vending Machine!\n")

def return_change(user_payment, price):
    change = user_payment - price
    if change > 0:
        print(f"Your change is £{change:.2f}.")

def main():
    while True: 
        menu_list()
        user_choice = input("Enter product code (or 'Q' to quit): ")
        if user_choice.lower() == 'q':
            break
        
        product = menu.get(user_choice)
        
        if product:
            if product["stock"] > 0:
                user_payment = ask_payment(user_choice)
                return_change(user_payment, product["price"])
                dispense_product(user_choice)
            else:
                print("Sorry, this product is out of stock.\n")
        else:
            print("Invalid product code.\n\n") 
        
    
if __name__ == "__main__":
    main()