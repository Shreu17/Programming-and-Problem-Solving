"""n = int(input())

if n > 0:
	fib_series = fibonacci_module.generate_fibonacci_sequence(n)
	print(' '.join(map(str, fib_series)))
else:
	print("Please enter a positive integer")            """
def generate_fibonacci_sequence(max_value):
	a, b = 0, 1
	result = []
	while a <= max_value:
		result.append(a)
		a, b = b, a + b
	return result
n = int(input())
if n <= 0:
	print("Please enter a positive integer")
else:
	seq = generate_fibonacci_sequence(n)
	print(" ".join(map(str, seq)))
