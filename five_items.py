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

        # Actions to execute
        Item.all.append(self)

    # Methods inside a class
    def calculate_total_price(self):
        return self.price * self.quantity

    def get_name(self):
        print(self.name)

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("iPhone 14", 100, 5)
item2 = Item("iPhone 15", 100, 5)
item3 = Item("iPhone 16", 100, 5)
item4 = Item("iPhone 17", 100, 5)
item5 = Item("iPhone 18", 100, 5)

print(Item.all)


