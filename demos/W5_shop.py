def shop():
    items = {"bread": 1.99, "eggs": 3.49, "milk": 1.99, "chicken": 7.99, "cheese": 2.49, "ham": 3.99}
    return items


def view_all(products = {}):
    for i, j in products.items():#Method "items" allows you to acces both keys and values in a pair
        print(f"{i}---------£{j}")


def playing():
    d = shop()
    d["cheese"] = 3
    d["milk"] = 1.69
    del d["eggs"]
    prod = input("Enter new product: ")
    price = float(input(f"Enter it's price:"))
    d[prod] = price
    view_all(d)


def basket():
    b = []
    while True:
        product = input("Enter an item or \"stop\": ")
        if product.upper() == "STOP":
            break
        q = int(input(f"Enter the quantity of {product}: "))
        for i in range(q):
            b.append(product)
    return b


def till(basket = []):
    all_items = shop()
    total = 0
    for product in basket:
        if product.lower() in all_items:
            total += all_items[product]
        else:
            print(f"No luck. The {product} is not sold here")
    return total


def run():
    print("Welcome to Mitko's shop. Please look around. We are watching you.")
    view_all(shop())
    b = basket()
    while True:
        response = input("Are you ready to pay [y/n]")
        if response[0].lower() == "y":
            to_pay = till(b)
            print(f"Pay £{to_pay:.2f} or I will come after you!!!")
            break
        else:
            b2 = basket()
            b.extend(b2)


run()


