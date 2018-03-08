# 5 - Menor Multiplo
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ATENÇÃO - Esse algoritmo encontra a resposta, mas esta muito lento, sera retrabalhado no futuro
divisores = 0
count = 1
numero = 1
while(divisores!=20):
	if(numero % count == 0):
		divisores = divisores + 1
		count = count + 1
		#numero = numero + 1
	else:
		divisores = 0
		numero = numero + 1
		count = 1
	print("Numero:",numero,"Divisores:",divisores,"Count:",count)
	#print(divisores)
	#print(count)
		
		
