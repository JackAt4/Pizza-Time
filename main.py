"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Aiden Stark
"""

import order
import checkout
import inventory

print("Welcome to Pizza Time!")
print("Select an option below")
print(" 1. Order \n 2. Checkout \n 3. Inventory \n 4. Exit")

while True:
    selection = input(">> ")
    if selection == "1":
        order.start()
    elif selection == "2":
        checkout.start()
    elif selection == "3":
        inventory.start()
    elif selection == "4":
        print("Goodbye!")
        break
    else:
        print("Not an option")
