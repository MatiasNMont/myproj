from random import randint
n=0
while n < 3:
	number = randint(0,10)
	number_user = int(raw_input("Ingrese Number:"))
	if number == number_user:
		break
	else:
		n+=1
else:
	print "Perdiste"
	

