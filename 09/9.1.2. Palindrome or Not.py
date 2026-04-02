St=input()
l=len(St)
f=True
for i in range (l//2):
	if St[i]!=St[l-1-i]:
		f=False
		break
	
if f:
	print("Palindrome")
else:
	print("Not a Palindrome")
