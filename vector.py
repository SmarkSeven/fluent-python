from math  import hypot

class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return 'Vector({0}, {1})'.format(self.x, self.y)
		
	def __abs__(self):
		return hypot(self.x, self.y)
	
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
		
	def __bool__(self):
		return bool(abs(self))
		
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)

a = Vector(1, 2)
b = Vector(2, 2)

print(abs(a + b))
		