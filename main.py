import csv

class Item:

    # Initializing a class attributes
    pay_rate = 0.8
    all = []

    # Defining a constructor- a magic method with __ __
    def __init__(self, name: str, price: float, quantity=0):

        # Run Validation inside class -> This will throw an assertion error and custom messages
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assigning class variables
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    # Methods inside a class
    def calculate_total_price(self):
        return self.price * self.quantity

    # Demonstration of class method or static method-> use decorator-> cls stands for class itself reference as object
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item.get('name'),price=int(item.get('price')),quantity=int(item.get('quantity')))

    def get_name(self):
        print(self.name)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

    @staticmethod
    def is_integer(num):
        # counting the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


# item1 = Item("iPhone 14", 100, 5)
#
#
# print(Item.__dict__) # Access all attributes from class level
# print(item1.__dict__) # Access all attributes from instance level

# item1.apply_discount()

# Searching attribute from class level since it wasn't found in instance level
# print(item1.price)
#
# item2 = Item("iPhone 15", 100, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

if __name__ == "__main__":
    Item.instantiate_from_csv()
    print(Item.is_integer(7.0))

# print(Item.all)

