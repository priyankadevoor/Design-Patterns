"""
Pizza class should be able to create a pizza with default base.
Should provide method to add toppings.
Then provide method to return the final pizza cost.
"""

class Topping:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price
    
class Base:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price 
    
class Pizza:
    def __init__(self, base):
        self.base = base
        self.toppings = []
    
    def add_topping(self, topping):
        self.toppings.append(topping)

    def cost(self):
        toppings_price = 0
        base_price = self.base.get_price()
        for topping in self.toppings:
            toppings_price += topping.get_price()
        return base_price+toppings_price

small_base = Base('small', 2)
medium_base = Base('medium', 3)
peppers = Topping('peppers', 1)
cheese = Topping('cheese', 1.5)
onions = Topping('onions', 1)
small_pizza = Pizza(small_base)
small_pizza.add_topping(cheese)
small_pizza.add_topping(peppers)
small_pizza.add_topping(onions)

print(small_pizza.cost())



