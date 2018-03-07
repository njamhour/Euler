# 4 - Numero Palindromo
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
a = 1
b = 1
aux = 0
#array = [0,0]
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
		if(d > 900000):
			print(d)
#	else:
#		print(last)
	

	#for c in range(a,99):
	#d = a * b
	#a += 1
	#print(d)
	#print("A:", a, " B:", b)
	#if(a>b):
	#b += 1
	#print("A:", a, " B:", b)
	#d = a * b
	#print(d)
#while(a<=99 and b>=1):
#c = a * b
#palindromo = str(c)
#if(palindromo==palindromo[::-1]):
#print palindromo
#a += 1
#b -= 1
	


	#if(a == b):
	#a += 1
	#else:
	#b =-1
	#c = a * b
	#b +- 1
	#print(c)
	#palindromo = str(c)
	#if(palindromo == palindromo[::-1]):
	#print(palindromo)
	#else:
	#b += 1
	#a += 1
	#hile(b<=99):
	#c = a * b
	#print(a, b)
	#a += 1
	#b += 1
	#print(c)
	#palindromo = str(c)
	##teste = palindromo[:::-1]
	#if(palindromo == palindromo[::-1]):
	#	print(palindromo)
	
