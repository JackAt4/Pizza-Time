import pandas

def start():
    print("This is the pizza ordering system")
    pizza_menu = pandas.read_csv("data/types.csv")
    print(pizza_menu)