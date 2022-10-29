import csv
class item:
    pay_rate = 0.8 #the price after discount
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        # run validations
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity
        #actions to execute
        item.all.append(self)

    def calculate(self):
        return self.price*self.quantity
    def discount(self):
        self.price = self.price*self.pay_rate
    @classmethod
    def instance_csv(cls):
        with open('./ items_.csv','r')as f:
            reader = csv.DictReader(f)
            items =list(reader)
        for item in items:
            print(item)
        
    def __repr__(self):
        return f"item('{self.name}',{self.price})"
        
item.instance_csv()
# item1 = item("Phone", 100, 1)
# item2 = item("Laptop", 1000, 3)
# item3 = item("Cable", 10, 5)
# item4 = item("Mouse", 50, 5)
# item5 = item("Keyboard", 75, 5)
# print(item.all)
# for instance in item.all:
#     print(instance.price)
