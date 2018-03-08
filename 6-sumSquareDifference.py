# 6 - Diferença entre soma de quadrados
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
a = 1
b = 0
c = 0
d = 0
totalA = 0
totalB = 0
while(a<=100):	
	b = b + a ** 2
	c = c + a
	d = c ** 2
	a = a + 1
print(b)
print(d)
totalA = d - b
print(totalA)