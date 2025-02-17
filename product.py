class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total = 0

    def show_products(self, products):
        print("Available Products:")
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product.name} - ${product.price}")

    def add_to_cart(self, product):
        self.cart.append(product)
        self.total += product.price
        print(f"{product.name} added to cart. Total: ${self.total}")

    def purchase(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Purchase successful. Items bought:")
            for product in self.cart:
                print(f"- {product.name} - ${product.price}")
            print(f"Total amount: ${self.total}")
            self.cart.clear()
            self.total = 0

    def cancel_order(self):
        if not self.cart:
            print("Your cart is already empty.")
        else:
            self.cart.clear()
            self.total = 0
            print("Order canceled. Your cart is now empty.")

# Sample products
products = [Product("Laptop", 1000), Product("Phone", 500), Product("Headphones", 100)]

# Shopping cart instance
cart = ShoppingCart()

# Example usage
cart.show_products(products)
cart.add_to_cart(products[0])  # Adding Laptop to cart
cart.add_to_cart(products[1])  # Adding Phone to cart
cart.purchase()
cart.cancel_order()
