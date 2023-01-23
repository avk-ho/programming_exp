# https://www.programmingexpert.io/projects/async-point-of-sale-system

# burger combo reduction of 15%
# burger combo is 1 burger, 1 side, 1 drink
# if multiple items are ordered, combo reduction applies on the most expensive items
# tax is 5% of the order

# user must be allowed to command without delay

import asyncio
from inventory import Inventory

TAX_RATE = 0.05
COMBO_REDUCTION = 0.85

### FUNCTION PROVIDED BY THE TEMPLATE
def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")

###
def collect_item_id_order(inventory):
    order_ids = []
    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    end_order = False
    while not end_order:
        item_id_order = input("Enter an item number: ")

        if item_id_order == "q":
            end_order = True
            continue

        try:
            item_id_order = int(item_id_order)
        except:
            print("Please enter a valid number.")
            continue

        max_id = len(inventory.items)
        valid_id = 0 < item_id_order < max_id + 1

        if not valid_id:
            print(f"Please enter a number below {max_id + 1}.")
            continue

        order_ids.append(item_id_order)

    return order_ids


def find_most_expensive_item(inventory, list_of_ids):
    most_exp_item_id = 0
    for id in list_of_ids:
        if most_exp_item_id == 0:
            most_exp_item_id = id
        
        most_exp_item = inventory.items[most_exp_item_id]
        item = inventory.items[id]
        if most_exp_item["price"] < item["price"]:
            most_exp_item_id = id
    
    return most_exp_item_id


# creates a combo, calculates and returns its price
def add_combo_price(inventory, burgers, sides, drinks):
    most_exp_burger_id = find_most_expensive_item(inventory, burgers)
    most_exp_side_id = find_most_expensive_item(inventory, sides)
    most_exp_drink_id = find_most_expensive_item(inventory, drinks)

    burgers[most_exp_burger_id] -= 1
    sides[most_exp_side_id] -= 1
    drinks[most_exp_drink_id] -= 1

    if burgers[most_exp_burger_id] < 1:
        del burgers[most_exp_burger_id]
    if sides[most_exp_side_id] < 1:
        del sides[most_exp_side_id]
    if drinks[most_exp_drink_id] < 1:
        del drinks[most_exp_drink_id]

    burger = inventory.items[most_exp_burger_id]
    side = inventory.items[most_exp_side_id]
    drink = inventory.items[most_exp_drink_id]

    combo_price = round((
        burger["price"] + side["price"] + drink["price"]) * COMBO_REDUCTION, 2)

    side_name = side["size"] + " " + side["subcategory"]
    drink_name = drink["size"] + " " + drink["subcategory"]

    print(f"${combo_price} Burger Combo")
    print(f"  {burger['name']}")
    print(f"  {side_name}")
    print(f"  {drink_name}")

    return combo_price

# item_dict must be either the burgers, sides or drinks dict (id:quantity)
def add_items_price(inventory, item_dict):
    price_to_add = 0
    for id, quantity in item_dict.items():
        item = inventory.items[id]
        price_to_add += (item["price"] * quantity)
        
        if item["category"] == "Burgers":
            print(f'${item["price"]} {item["name"]} * {quantity}')
        else:
            item_name = item["size"] + " " + item["subcategory"]
            print(f'${item["price"]} {item_name} * {quantity}')

    return price_to_add

# receives the ids from collect_item_id_order()
# returns a tuple of dicts (burgers, sides, drinks)
# each dict is {id:quantity}
async def place_orders(inventory, order_ids):
    print("Placing order...")

    items_info = []
    items_in_stock = []
    # items_stock = []

    # doing the creation of task and the gathering in 2 steps makes the process
    # faster
    for id in order_ids:
        info = asyncio.create_task(inventory.get_item(id))
        in_stock = asyncio.create_task(inventory.decrement_stock(id))
        # stock = asyncio.create_task(inventory.get_stock(id))

        items_info.append(info)
        items_in_stock.append(in_stock)
        # items_stock.append(stock)

    # print(inventory.items)

    # (bool, dict) pairs
    items = []
    for i in range(len(items_info)):
        # remove stock
        order = await asyncio.gather(items_in_stock[i], items_info[i]) # ,items_stock[i]
        items.append(order)

    print(items)
    
    burgers = {}
    sides = {}
    drinks = {}
    for item in items:
        id = item[1]["id"]
        if item[0]:
            category = item[1]["category"]

            if category == "Burgers":
                burgers[id] = burgers.get(id, 0) + 1
            elif category == "Sides":
                sides[id] = sides.get(id, 0) + 1
            elif category == "Drinks":
                drinks[id] = drinks.get(id, 0) + 1
        else:
            print(
                f"Unfortunately item number {id} is out of stock and has been removed from your order. Sorry!")

    return (burgers, sides, drinks)


def calculate_total_order_price(inventory, burgers, sides, drinks):
    num_of_combos = min(len(burgers), len(sides), len(drinks))

    subtotal = 0.00

    print("Here is a summary of your order: \n")

    while num_of_combos > 0:
        subtotal += add_combo_price(inventory, burgers, sides, drinks)

        num_of_combos -= 1

    subtotal += add_items_price(inventory, burgers)
    subtotal += add_items_price(inventory, sides)
    subtotal += add_items_price(inventory, drinks)

    tax = round(subtotal * TAX_RATE, 2)
    total_price = round(subtotal + tax, 2)
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total_price}")

    return total_price


def conclude_order(total_price):
    valid_confirm_order = False
    while not valid_confirm_order:
        confirm_order = input(
            f"Would you like to purchase this order for ${total_price} (yes/no)? ")
        if confirm_order == "yes":
            print("Thank you for your order!")
            valid_confirm_order = True
        elif confirm_order == "no":
            print("No problem, please come again!")
            valid_confirm_order = True
        else:
            print("Invalid input.")

    valid_new_order = False
    while not valid_new_order:
        do_new_order = input(
            "Would you like to make another order (yes/no)? ")
        if do_new_order == "yes":
            valid_new_order = True
            continue_new_order = True
        elif do_new_order == "no":
            print("Goodbye!")
            valid_new_order = True
            continue_new_order = False
        else:
            print("Invalid input.")

    return continue_new_order


async def main():
    print("Welcome to the ProgrammingExpert Burger Bar!")

    inventory = Inventory()

    print("Loading catalogue...")
    catalogue = await inventory.get_catalogue()
    display_catalogue(catalogue)

    continue_new_order = True
    while continue_new_order:
        order_ids = collect_item_id_order(inventory)
        
        burgers, sides, drinks = await place_orders(inventory, order_ids)

        total_price = calculate_total_order_price(inventory, burgers, sides, drinks)

        continue_new_order = conclude_order(total_price)


if __name__ == "__main__":
    asyncio.run(main())