class item:
    def __init__(self, name: str, price: float, quantity=0):
        # run validations
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        return self.price*self.quantity


item1 = item("phone", 100, -1)
print(item1.name)
print(item1.calculate())
