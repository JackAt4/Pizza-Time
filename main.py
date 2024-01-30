"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Aiden Stark
"""
import order, checkout
from os import system

customer_order = []
while True:
    system("cls")
    
    print("Welcome to Pizza Time!")
    print("Select an option below")
    print(" 1. Order \n 2. Checkout \n 3. Exit")
    selection = input(">> ")
    if selection == "1":
        system("cls")
        customer_order = order.start()
    elif selection == "2":
        if len(customer_order) > 0:
            system("cls")
            checkout.start(customer_order)
        else:
            print("Cart is empty, go to Order")
    elif selection == "3":
        print("Goodbye!")
        break
    else:
        print("Not an option")
