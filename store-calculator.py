class Product:
	price = 0
	count = 0
	tax = 1
	name = ""
	def __init__(self, price, count, tax, name):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = name

	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total

products = [
	Product(price=900, count=2, tax=1.25, name="Robot"), 
	Product(price=100, count=1, tax=1.06, name="Bok"), 
	Product(price=350, count=2, tax=1.25, name="Reservdel")
]

total_price = 0

for product in products:
	total_price += product.price_with_tax()

for product in products:
	print(product.name, product.price_with_tax())

print("Totalpris", total_price)
