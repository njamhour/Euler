# 3 - Maior Primo
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

numero = 600851475143
#numero = 10000
fatorial = 1
c = 1
divisor = 0

while(fatorial < numero):
	if(numero % fatorial == 0):
		#print(fatorial, " divisor")	
		while(c < fatorial):
			if(fatorial % c == 0):
				divisor = divisor + 1
			c = c + 1
		if(divisor < 2):
			print("Primo", fatorial)
			divisor = 0
		c = 1
	fatorial = fatorial + 1			 
