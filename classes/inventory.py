from classes.product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    @property
    def products(self):
        return self.__products

    def add(self,product):
        if not isinstance(product,Product):
            raise ValueError("product must be instanse of class Product")
        if self.__products:
            for p in self.__products:
                if p.name == product.name:
                    raise ValueError(f"{p.name} already exists")
        self.products.append(product)


    def find(self,product):
        if self.products:
            for p in self.products:
                if p.name == product:
                    return p
        return None

    def by_value(self):
        if self.products:
            sorted_products = sorted(self.products,key = lambda p: p.total_value,reverse=True)
            return sorted_products
        return None
    
    @property
    def total_value(self):
        count = 0
        for product in self.__products:
            count += product.total_value
        return count
