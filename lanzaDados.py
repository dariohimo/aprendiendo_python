import random

juegos = 0
bandera = True

print("Bienvenido a lanzar dados!!!")

while bandera:
	# dos datos para lanzar.
	dado1 = random.randint(1,6)
	dado2 = random.randint(1,6)
	
	#suma de lanzamientos de dados
	valordados = dado1 + dado2
	
	print(f"\nLanzamiento: \t{dado1}\t{dado2}")
	juegos += 1
	print(f"\nsuma de los dados:  {valordados} ; Lanzamientos:  {juegos} ")
	
	#empieza el input para validad el if si sigue jugando.
	jugando1 = input("\nSEGUIR JUGANDO S/N: ")
	
	
	#string.upper  aqui vuelve los caracteres a minuscula.
	if jugando1.lower() == 's' :   
		bandera = True
			
	else:
		print("\nGracias por jugar!!!")
		bandera = False
