class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi,I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder
    
class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order.items} to {order.costumer} using {self.vehicle}.")
        order.status = 'delivered'

class DeliveryOrder:
    def __init__(self, costumer, items):
        self.costumer = costumer
        self.items = items
        self.status = 'preparing'
    
    def assign_driver(self, driver):
        return driver

    def summary(self):
        return f"Order Summary:\nItem: {self.items}\nCostumer: {self.costumer.name}\nStatus: {self.status}\nDriver: {self.assign_driver().name}"

#main code
#create 2 customers
person1 = Customer('Alice', 'house A')
person2 = Customer('Bob', 'house B')
#create 1 driver
person3 = Driver('David', 'motorcycle')
#introduce themself
person1.introduce()
person2.introduce()
person3.introduce()
print()
#each person order an order
order1 = DeliveryOrder(person1, 'Laptop')
order2 = DeliveryOrder(person2, 'Headphones')
order1.summary()
print()
order2.summary()
print()
#driver is assign to dliver the orders
person3.deliver(order1)
person3.deliver(order2)
print()
#finalize the process
