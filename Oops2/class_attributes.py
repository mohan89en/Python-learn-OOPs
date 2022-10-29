class item:
    pay_rate = 0.8 #the price after discount
    def __init__(self, name: str, price: float, quantity=0):
        # run validations
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        return self.price*self.quantity
    def discount(self):
        self.price = self.price*self.pay_rate
item1 = item("phone",100,1)
print(item1.__dict__)
item1.discount()
print(item1.price)
item2 = item("laptop",2000,2)
item2.pay_rate =0.7
item2.discount()
print(item2.price)


