
a = set(map(int, input("Set A: ").split()))

b = set(map(int, input("Set B: ").split()))

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

