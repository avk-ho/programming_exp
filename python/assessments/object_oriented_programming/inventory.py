# https://www.programmingexpert.io/object-oriented-programming/assessment/1

class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.items = {}

    def add_item(self, name, price, quantity):
        if name in self.items or \
        self.max_capacity < self.current_capacity + quantity:
            return False
    
        self.items[name] = {
            "price": price,
            "quantity": quantity
        }
        self.update_capacity(quantity)
        return True

    def delete_item(self, name):
        if name in self.items:
            self.current_capacity -= self.items[name]["quantity"]
            del self.items[name]
            return True
        else:
            return False

    def update_capacity(self, quantity):
        self.current_capacity += quantity

    def get_items_in_price_range(self, min_price, max_price):
        items = []
        
        for item in self.items:
            price = self.items[item]["price"]
            if min_price <= price <= max_price:
                items.append(item)
           
        return items

    def get_most_stocked_item(self):
        if len(self.items) == 0:
            return None
        
        max_item = ""
        max_quantity = 0
        for item in self.items:
            quantity = self.items[item]["quantity"]
           
            if quantity > max_quantity:
                max_item = item
                max_quantity = quantity

        return max_item