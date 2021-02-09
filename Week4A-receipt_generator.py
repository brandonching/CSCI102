# Brandon Ching
# ​CSCI 102 – Section C
# Week 4 - Lab A - Receipt Generator
# References: N/A
# Time: 10 minutes

company_name = input("Enter company name:")
location = input("Enter company city/state:")
cashier_name = input("Enter cashier name:")
item1 = input("Purchased item 1 name:")
price1 = input("Purchased item 1 price:")
item2 = input("Purchased item 2 name:")
price2 = input("Purchased item 2 price:")
item3 = input("Purchased item 3 name:")
price3 = input("Purchased item 3 price:")
ending_message = input("Enter your favorite ending message:")

total_cost = float(price1) + float(price2) + float(price3)
print(
    f"        RECEIPT GENERATOR\n"
    f"===================================\n"
    f"  {company_name}\n"
    f"  {location}\n"
    f"***********************************\n"
    f"  Your cashier was: {cashier_name}\n"
    f"  Welcome Valued Customer\n"
    f"***********************************\n"
    f"  Item Name       Item Price\n\n"

    f"  {item1}             ${price1}\n"
    f"  {item2}             ${price2}\n"
    f"  {item3}             ${price3}\n\n"
        
    f"***********************************\n"
    f"  Total Cost of Order: {total_cost:.2f}\n"
    f"***********************************\n"
    f"  {ending_message}\n"
    f"==================================="
    )   
