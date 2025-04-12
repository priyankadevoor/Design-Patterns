from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_operation(self, data):
        pass

class ConcreteStrategy1(Strategy):
    def do_operation(self, data):
        print('Strategy1')
        return sorted(data)

class ConcreteStrategy2(Strategy):
    def do_operation(self, data):
        print('Strategy2')
        return reversed(sorted(data))

class Context:
    def __init__(self, strategy):
        self._strategy = strategy
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def do_business_logic(self):
        result = self._strategy.do_operation(["a", "b", "c", "d", "e"])

#In main directly create objects to each different algo and call their do_operation.

algo1 = ConcreteStrategy1()
context = Context(algo1)
context.do_business_logic()
#Now using setter you can change in runtime 
context.strategy = ConcreteStrategy2()
context.do_business_logic()