class Item:
    # Defining a constructor- a magic method with __ __
    def __init__(self, name: str, price: float, quantity=0):

        # Run Validation inside class -> This will throw an assertion error and custom messages
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assigning class variables
        self.name = name
        self.price = price
        self.quantity = quantity

    # Methods inside a class
    def calculate_total_price(self):
        return self.price * self.quantity

    def get_name(self):
        print(self.name)


item1 = Item("iPhone 14", 999, 5)

item2 = Item("iPhone 15", 1299, 3)
