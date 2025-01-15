# menu variables
menu = ("cup noodles", "chips", "croissant", "orange juice", "iced americano", "karak tea")
# menu_price = [AED10, AED5, AED2.50, AED3.50, AED5, AED1]

# welcome message
print("Hey there! Welcome to Hamartia Vending Machine!")
# menu 
print("""MENU:\n
      Snacks:\t\t\t Drinks:
      0 - cup noodles\t\t 3 - orange juice
      1 - chips\t\t\t 4 - iced americano
      2 - croissant\t\t 5 - karak tea\n""")

order_code = int(input("What can I get for you today? Please enter the order code.\n"))
user_order = menu[order_code]
user_bill = 0
print(f"One {user_order} coming right up!")

# while order_code >= 0 and order_code <= 5:    
if order_code == 0:
        user_bill += 10
        print(f"The {user_order} cost AED 10")
elif order_code == 2:
        user_bill += 2.50
        print(f"The {user_order} cost AED 2.50")
elif order_code == 3:
        user_bill += 3.50
        print(f"The {user_order} cost AED 3.50")
elif order_code == 5:
        user_bill += 1
        print(f"The {user_order} cost AED 1")
elif order_code < 1 or order_code > 5:
        print("You put the wrong number")
else:
        user_bill+= 5
        print(f"The {user_order} cost AED 5")
        
add_item = (input("Would you like to purchase another item?\n"))
if add_item.lower == "Yes":
    print(input("Enter your code: "))
elif add_item.lower == "No":
    print("okie")
        
user_payment = float(input("Please enter the correct amount: "))
if user_payment == user_bill:
    print("You paid the correct amount.")    
elif user_payment < user_bill:
    input("You paid short. Please pay the correct amount: ")
    if user_payment == user_bill:
        print("You paid the correct amount.")
else:
    print("You paid more than the amount asked. Please wait for the change.")
    change = user_payment - user_bill
    print(f"Your change is AED {change:.2f}. Thank you for using our services!")