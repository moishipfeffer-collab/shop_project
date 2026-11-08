class Product:
    def __init__(self,name,price,quantity = 0):
        self.__name = name 
        self.__price = price 
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if self.__price <= 0:
            raise ValueError("price must be positive")
        self.__price = new_price

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self,sell_num):
        self.__quantity = sell_num

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if new_price < 1:
            raise ValueError("price must be positive")
        self.__price = new_price

    
    def add_stock(self,stock_num):
        if stock_num <= 0:
            raise ValueError("amont must be positive")
        self.__quantity += stock_num

    def sell(self,sell_num):
        if self.quantity - sell_num < 0:
            raise ValueError(f"not enough {self.name}")
        self.quantity -= sell_num
        
    @property
    def total_value(self): 
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name}: {self.quantity} x {self.price} = {self.total_value}"



