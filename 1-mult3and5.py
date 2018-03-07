# 1 - Multiplos de 3 e 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
x, totalA, totalB, totalC = 1,0,0,0
while(x<1000):
	if(x % 3 == 0):
		totalA = totalA + x
		x = x + 1
	elif(x % 5 == 0):
		totalB = totalB + x
		x = x + 1
	else:
		x = x + 1
print("Soma multiplos 3: ", totalA)
print("Soma multiplos 5: ", totalB)
totalC = totalA + totalB
print("Soma total = ", totalC)
		