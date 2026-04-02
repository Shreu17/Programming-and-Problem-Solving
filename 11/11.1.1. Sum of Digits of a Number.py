num = int(input("Enter a number: "))
temp = num
digit_sum = 0
while temp > 0:
	digit = temp % 10
	digit_sum += digit
	temp //= 10
print("Sum of digits:", digit_sum )
