# import random

class Product():
    def __init__(code, name, price, stock, category):
        code.name = name
        code.price = price
        code.stock = stock
        code.category = category

HF01 = Product("Cup Noodles", 10.00, 11, "Hot Food")
HF02 = Product("Cup Noodles", 10.00, 11, "Hot Food")
S01 = Product("Cup Noodles", 10.00, 11, "Hot Food")
S02 = Product("Cup Noodles", 10.00, 11, "Hot Food")
S03 = Product("Cup Noodles", 10.00, 11, "Hot Food")


# # a menu of drinks and snacks presented via the console
# menu = {
#     # a set of numbers or codes that the user can input to select a particular drink or snack
#     # categorising items in the vending machin to improve user experience
#     # a stock system meaning the machine may run out of products
#     "HF01": {"name": "Cup Noodles", "price": 10.00, "stock": 11, "category": "Hot Food"},
#     "HF02": {"name": "Hot Pockets", "price": 15.00, "stock": 9, "category": "Hot Food"},
#     "S01": {"name": "Chips", "price": 5.00, "stock": 4, "category": "Snacks"},
#     "S02": {"name": "Croissant", "price": 2.50, "stock": 10, "category": "Snacks"},
#     "S03": {"name": "Chocolate", "price": 1.99, "stock": 15, "category": "Snacks"},
#     "CD01": {"name": "Orange Juice", "price": 3.50, "stock": 7, "category": "Cold Drinks"},
#     "CD02": {"name": "Iced Americano", "price": 5.00, "stock": 5, "category": "Cold Drinks"},
#     "CD03": {"name": "Soda", "price": 5.00, "stock": 14, "category": "Cold Drinks"},
#     "HD01": {"name": "Karak Tea", "price": 1.00, "stock": 3, "category": "Hot Drinks"}
# }

# def menu_list(): # this is where the menu will be displayed
#     print("╭────────────────────────────────────────────────────.★..─╮\n\n" +
# """\t╭───────────────────༺♡༻──────────────────╮
# \t   Welcome to Hamartia Vending Machine!
# \t╰────────────────────────────────────────╯\n\n""") # display of the vending machine name
#     menu_title = "⋆ ˚｡⋆୨ ʚ MENU ɞ ୧⋆ ˚｡⋆" # menu header variable
#     print(f'{menu_title:^55}') # centering the menu header
#     print("     ╭ \t\t\t\t\t\t    ╮")
#     for code, product in menu.items(): # displaying the products one by one until the list ends
#         # centered format of the menu display
#         print(f"\t{code}: {product['name']:^14} - £{product['price']:.2f} ({product['stock']} in stock)") 
#     print("     ╰ \t\t\t\t\t\t    ╯")
#     print("\n")
    
# # a way of managing the money so the user can input any amount of money and have the correct change returned
# def ask_payment(user_choice): # the parameter is the code that the user chose from the menu
#     user_payment = 0 # setting the user payment to zero
#     product = menu[user_choice] # the product variable is set based on the user choice input
#     price = product["price"] # the price variable is set based on the product's price in the list
#     if user_payment != price: # if the user payment does not match the product price it will continue asking the user for payment
#         # prompt to ask user for payment and the bill will be the amount of money the user inputted
#         bill = float(input("Please insert the correct amount in coins or notes: £")) 
#         user_payment += bill # user_payment will increase as the user pays their bill
#     return user_payment # prints the user's payment
        
# # an intelligence system for suggesting purchases
# def suggest_product(last_purchase): # the parameter is the user's last purchase
#     if last_purchase["category"] == "Hot Drinks" or last_purchase["category"] == "Cold Drinks":
#         suggestions = ["S01", "S02", "S03"] # if the product purchased is a drink then the machine will suggest a snack
#     elif last_purchase["category"] == "Snacks":
#         suggestions = ["CD01", "CD02", "CD03", "HD01"] # if the product purchased is a snack then the machine will suggest a drink
#     else:
#         suggestions = ["CD01", "CD03"] # if the product purchased is a hot food then the machine will suggest a cold drink
#     return random.choice(suggestions) # randomizes the selection of suggestions within a certain category of products
        
# def dispense_product(user_choice): # the parameter is the code that the user chose from the menu
#     product = menu[user_choice]
#     name = product["name"]
#     if product["stock"] > 0: # as long as the stock is greater than one it will continue its service
#         product["stock"] -= 1 # the product stock will be reduced by 1 whenever the user purchases it
#         print(f"\nDispensing {name}...")
#         print(f"{name} dispensed.") # a message that tells the user that a particular drink or snack has been dispensed
#         print("\nThank you for using Hamartia Vending Machine!\n")
#     else:
#         print("Sorry, this product is out of stock.") # a message that tells the user that a product is out of stock
#         print("\nThank you for using Hamartia Vending Machine!\n")
        
# def short_payment(user_payment, price): # the parameter is the user's payment and the price of the product
#     short_amount = price - user_payment
#     while user_payment < price: # if the user payment is less than the price of the product, it will continue asking for payment
#         print(f"You are £{short_amount} short.") # a message that tells the user how much money they need to add if they paid short
#         # asks for the missing amount of money and stores it in remaining_amt variable
#         remaining_amt = float(input("Please pay the remaining amount: £"))
#         user_payment += remaining_amt # adds the remaining amount to the user's payment

# def return_change(user_payment, price): # the parameter is the user's payment and the price of the product
#     change = user_payment - price # change is the payment subtracted by the price
#     if change > 0: # if the change is greater than zero then there will be change given
#         print(f"Your change is £{change:.2f}.") # a message that tells the user how much change they have received

# def main(): # main interface
#     last_purchase = None # the last_purchase determines what product will be suggested after purchasing
#     while True: # ensures that the code will not finish unless the user will input 'q' 
#         menu_list()
#         # a way of allowing users to buy additional items; the code will not finish executing unless the user types 'q'
#         user_choice = input("Enter product code (or 'Q' to quit): ") 
#         if user_choice.lower() == 'q':
#             print("\n╰─..★.────────────────────────────────────────────────────╯") # prints if the user inputs 'q' to break the code
#             break # ends the code
        
#         # sets the product variable to what the code the user inputted from the menu
#         product = menu.get(user_choice)
        
#         if product:
#             # if the product's stock is greater then zero it will commence the following lines of code
#             if product["stock"] > 0:
#                 user_payment = ask_payment(user_choice)
#                 short_payment(user_payment, product["price"]) # pulls the short_payment code in the main code
#                 return_change(user_payment, product["price"]) # pulls the return_change code in the main code
#                 dispense_product(user_choice) # pulls the dispense_product code in the main code
#                 last_purchase = product # the last_purchase variable will be updated to the product the user just purchased
#                 suggestion = suggest_product(last_purchase) # pulls the suggest_product code in the main code based on the last_purchase
#                 print(f"Consider buying {menu[suggestion]["name"]} for your next purchase.\n") # prints the suggestion
#                 print("╰─..★.────────────────────────────────────────────────────╯")
#             else:
#                 print("Sorry, this product is out of stock.\n") # prints if the the product's stock is less than or equal to zero
#                 print("╰─..★.────────────────────────────────────────────────────╯")
#         else:
#             print("Invalid product code.\n\n" + 
#                   "╰─..★.────────────────────────────────────────────────────╯") # prints if the user inputs the wrong product code
        
    
# if __name__ == "__main__":
#     main()