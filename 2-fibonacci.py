# 2 - Fibonacci
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
a = 1
b = 2
c = 0
soma = 0
while(a<4000000):
	c = a
	a = b
	b = a + c
	if(c % 2 == 0):
		soma = soma + c
print(soma)