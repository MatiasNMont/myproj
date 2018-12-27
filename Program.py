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
	
rock = {
	"Actor A":[],
	"Actor B":[],
	"Cant" : 0
	}
def num_even(lista):
	l=[]
	for i in lista:
		if i % 2 == 0:
			l.append(i)
	return l

def funcion():
	list = [ x for i in range(1,15) if x % 2 == 0]
	return list
	
print randint(0,100)
print funcion()
print "SOLO SON CAMBIOS PARA VER LAS RAMAS"
