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
        return DeliveryOrder(self.name, item)
    
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
        return f"Order Summary:\nItem: {self.items}\nCostumer: {self.costumer}\nStatus: {self.status}\nDriver: {self.assign_driver(person3).name}"

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
order1 = person1.place_order('Laptop')
order2 = person2.place_order('Headphones')
print(order1.summary())
print()
print(order2.summary())
print()
#driver is assign to dliver the orders
person3.deliver(order1)
person3.deliver(order2)
print()
#finalize the process
print('Final Status:')
print(f'Order for Laptop: {order1.status}')
print(f'Order for Headphone: {order2.status}')