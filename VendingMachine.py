S01 = "cheesecake"
S02 = "chips"
S03 = "croissant"
S04 = "donut"
S05 = "bread"
D06 = "strawberry latte"
D07 = "matcha latte"
D08 = "iced americano"
D09 = "banana milk"
D10 = "karak tea"

print("Hey there! Welcome to Hamartia Vending Machine!")
print("MENU:\n"
      "Snacks:\n"+
      S01+"\n"+
      S02+"\n"+
      S03+"\n"+
      S04+"\n"+
      S05+"\n"+
      "\nDrinks:\n"+ 
      D06+"\n"+
      D07+"\n"+
      D08+"\n"+
      D09+"\n"+
      D10+"\n")

order = input("What can I get for you today?\n")

print("\nOne " + order + " coming right up!")

input("Please enter the correct amount: ")
if (input < "7"):
    print("You paid the correct amount.")
    
if (input > "7"):
    print("You paid the incorrect amount.")