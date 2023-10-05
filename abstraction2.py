from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def display_details(self):
        pass
   

class Electronic(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def display_details(self):
        return f"Product Name: {self.name}\nPrice: ${self.price}\nBrand {self.brand}\nWarranty: {self.warranty}"
    
    def get_price(self):
        return f"\nPrice: ${self.price}"

class Clothing(Product):
    def __init__(self, name, price, size, color, material):
        super().__init__(name, price)
        self.size = size
        self.color = color
        self.material = material

    def display_details(self):
        return f"Product Name: {self.name}\nPrice: ${self.price}\nSize: {self.size}\nColor: {self.color}\nMaterial: {self.material}"
    
    def get_price(self):
        return f"\nPrice: ${self.price}"


class Books(Product):
    def __init__(self, name, price, author, genre):
        super().__init__(name, price)
        self.author = author
        self.genre = genre

    def display_details(self):
        return f"Product Name: {self.name}\nPrice: ${self.price}\nAuthor {self.author}\nGenre: {self.genre}"
    
    def get_price(self):
        return f"\nPrice: ${self.price}"
    


electronic_product = Electronic("Smartphone", 599.99, "Apple", "1 year")
clothing_product = Clothing("T-shirt", 19.99, "M", "Blue", "Cotton")
book_product = Books("Python Programming", 49.99, "John Smith", "Programming")


print("\n\nElectronic Product Details:")
print(electronic_product.display_details())
print(electronic_product.get_price())

print("\n\nClothing Product Details:")
print(clothing_product.display_details())
print(clothing_product.get_price())

print("\n\nBook Product Details:")
print(book_product.display_details())
print(book_product.get_price())

