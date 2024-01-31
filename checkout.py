def start(order):

    subtotal = 0
    tax_rate = 0.095

    print("Customer Order: ")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += int(i.quantity) * float(i.price)

    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    print("Subtotal: $" + str(subtotal))
    print("Tax = $" + str(tax))
    print("Total: $" + str(total))
    save(order, total)
    payment(total)

def payment(total):
    while True:
        payment_type = input("Cash or Credit? \n >> ")
        if payment_type.lower() == "cash":
            print(f"The total is ${total}.")
            cash = int(input("Enter cash received: "))
            change = round(cash - total, 2)
            print(f"Return ${change} to the customer.")
            input("(Press ENTER to continue)")
            break
        elif payment_type.lower() == "credit":
            print(f"The total is ${total}.")
            print("Please swipe the credit card")
            input("Press ENTER after completing the credit card Transaction")
            break
        else:
            print("Cash or Credit only.")
            input("(Press ENTER to continue)")

def save(order, total):
    with open("data.piza", "a") as orders:
        for i in order:
            orders.write(f"{i.type}, {i.size}, {i.quantity}, {i.price}, ")
        orders.write(f"{total}")
        orders.write("\n")