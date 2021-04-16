class OrderSL:
	def __init__(self, email, base, quote, date, time, order_type, side, b_amount, stop):
		self.email = email
		self.base = base
		self.quote = quote
		self.date = date
		self.time = time
		self.side = side
		self.b_amount = b_amount
		self.order_type = order_type
		self.stop = stop
