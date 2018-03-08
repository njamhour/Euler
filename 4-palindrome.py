# 4 - Numero Palindromo
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
a = 1
b = 1
aux = 0
auxDois = 0
while(a<=999 and b<=999):
	d = a * b
#	print(d)
	a += 1
	if(a == 999):
		b += 1
		a = 1
	palindromo = str(d)
	if(palindromo == palindromo[::-1]):
#		print(palindromo)
		if(auxDois == 0):
			auxDois = d
			#print(array[0])
		else:
			aux = d
			#print(array[1])
		if(auxDois < aux):
			auxDois = aux		
print(auxDois)