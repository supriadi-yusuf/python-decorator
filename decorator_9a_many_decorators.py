def wrapper1(item):
	def wrapped_item():
		return 'wrap box of "{}"'.format(str(item()))

	return wrapped_item

@wrapper1
def fungsi1():
	return 'ini fungsi 1'

def bungkus_lagi(item):
	def yg_di_bungkus():
		return 'yang dibungkus lagi : {}'.format(str(item()))

	return yg_di_bungkus

@bungkus_lagi
@wrapper1
@wrapper1
def fungsi2():
	return 'hello ... fungsi 2'

print fungsi1
print fungsi1()
print fungsi2()

print fungsi1.__name__
print fungsi2.__name__


