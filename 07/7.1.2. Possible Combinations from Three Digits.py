a, b, c = map(int, input().split())
digits = [a, b, c]
for i in range(3):
	for j in range(3):
		for k in range(3):
			if i != j and j != k and i != k:
				print(digits[i], digits[j], digits[k], sep="")
