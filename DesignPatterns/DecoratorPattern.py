from abc import ABC, abstractmethod

class CoffeeInterface:
    @abstractmethod
    def cost(self):
        pass

class Coffee(CoffeeInterface):
    def cost(self):
        return 5
    
class CoffeeDecorator(CoffeeInterface):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())  # Output: 8
