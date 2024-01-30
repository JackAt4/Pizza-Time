import pandas
import warnings

class Order:
    def __init__(self, quantity, size, type, price):
        self.quantity = quantity
        self.size = size
        self.type = type
        self.price = price[1:]

warnings.simplefilter(action='ignore', category=FutureWarning)

def start():

    order = []
    while True:
        print("Which pizza would you like to order?")
        pizza_menu = pandas.read_csv("data/types.csv")
        print(pizza_menu[["Type", "Size", "Price"]])
        
        selection = int(input(">> "))
        if len(pizza_menu) < selection + 1 or selection < 0:
            print("Invalid Choice")
            continue

        size = pizza_menu.iloc[selection][1]
        ptype = pizza_menu.iloc[selection][0]
        price = pizza_menu.iloc[selection][2]
        quantity = int(input(f"How many {size} {ptype} Pizzas do you want to order? \n>> "))

        order.append(Order(quantity, size, ptype, price))
        print("Would you like to order another pizza type? (y/n)")
        confirm = input(">> ")

        if confirm.lower() == "y":
            continue
        else:
            break

    for i in order:
        print(i.quantity, i.size, i.type, i.price)
    
    return order