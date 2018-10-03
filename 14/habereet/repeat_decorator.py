from functools import wraps

my_int = 7

def repeat(count):
	def real_decorator(func):
		def wrapper(*args, **kwargs):
			for _ in range(0, count):
				print(f'{func(*args, **kwargs)}')
		return wrapper
	return real_decorator

@repeat(my_int)
def get_text(text="I code with PyBites"):
	return text


get_text()