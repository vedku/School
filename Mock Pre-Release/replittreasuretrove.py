"""
Upon opening my replit account for the first time in 3 years, I was greeted by this gem from my pre release in 2020.
"""

#array to store the values
number_items = []
item_name = []
item_description = []
reserve_price = []
#array for the lists so I can append
number_items_list = []
item_name_list = []
item_description_list = []
reserve_price_list = []

number_items = int(input("How many items are you listing in the auction? \n(MUST BE AT LEAST 10)\ninput your answer here:"))
#error statement
while number_items <2:
    print("\n \n \nYou must have at least 10 items.")
    number_items = int(input("Let's try again. How many items are you listing in the auction? \n(MUST BE AT LEAST 10)\ninput your answer here:"))
for i in range(0, number_items):
    item_name = input("\n \n \n \n \nWhat is your item's name? \ninput your answer here:")
    item_name_list.append(item_name)
    item_description = input("\n \n \n \n \nWrite a short description of your item \ninput your answer here:")
    item_description_list.append(item_description)
    reserve_price = int(input("\n \n \n \n \nWhat is your reserve price?\ninput your answer here:"))
    reserve_price_list.append(reserve_price)
#reserve price error statement
if reserve_price < 1:
    int(input("\n \n \n \n \nReserve price must be more than 1.\ninput your answer here:"))
print("\n \nThe number of items you are auctioning is:",(number_items_list))
print("Your item name is:",(item_name_list))
print("A short description of the item is:",(item_description_list))
print("The least you would be willing to sell it for would be:",(reserve_price_list))
