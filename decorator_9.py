from functools import wraps

def wrapper1(item):
	def wrapped_item():
		return 'wrap box of "{}"'.format(str(item()))

	return wrapped_item

@wrapper1
def fungsi1():
	return 'ini fungsi 1'

def wrapper2(item):
	@wraps(item) # use origin function name in __name__ attribute
	def wrapped_item():
		return 'wrap box of "{}"'.format(str(item()))

	return wrapped_item

@wrapper2
def fungsi2():
	return 'ini fungsi 2'

print fungsi1
print fungsi1()
print fungsi2
print fungsi2()

print fungsi1.__name__
print fungsi2.__name__
