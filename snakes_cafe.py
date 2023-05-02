def welcoming_msg():
    print(
        """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
    )


def print_menu(menu):
    for category, item in menu.items():
        print("")
        print(f'{category}\n{"-----"}')
        print("\n".join(item))


def ordering():
    print(
        """
***********************************
** What would you like to order? **
***********************************
"""
    )


def ending_msg():
    print("thanks for using snakes cafe application !")


# i have added Grand Special Sauce and Baglawa just in order to make Mohammad Al Sa'ad feel Happy
menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": [
        "Salmon",
        "Steak",
        "Meat Tornado",
        "A Literal Garden",
        "Grand Special extra Sauce",
    ],
    "Desserts": ["Ice Cream", "Cake", "Pie", "Baglawa"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
}


welcoming_msg()
print_menu(menu)
ordering()

orders_dict = {}

while True:
    user_order = input("> ").title()
    if user_order == "Quit":
        break
    if user_order not in [item for sublist in menu.values() for item in sublist]:
        # if user_order not in menu.values():
        print("Sorry, that item is not on the menu.")
        continue
    if user_order in orders_dict:
        orders_dict[user_order] += 1
    else:
        orders_dict[user_order] = 1
    print(
        f'** {orders_dict[user_order]} order{"s" if orders_dict[user_order]>1 else ""} of {user_order} have been added to your meal **'
    )

ending_msg()
