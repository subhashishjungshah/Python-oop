from main import Item

# Phone class is inheriting from Item class


class Phone(Item):

    all = []

    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        # Call super function to have access to all attributes and methods
        super().__init__(name, price, quantity)

        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        self.broken_phones = broken_phones

        Phone.all.append(self)



phone1 = Phone("Iphone14", 999, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("Iphone15", 1299, 5, 2)
