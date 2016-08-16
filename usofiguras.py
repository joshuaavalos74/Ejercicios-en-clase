from cuadrado import Cuadrado
from triangulo import Triangulo
mi_trangulo=0
mi_cuadrado=0

print("Bienvenido a el creador de cuadrados, triangulos y calculador de sus areas. De Naruto.")
opc=int(input("Presione 1 para crear figura. \nPresione 2 para salir."))
while opc==1:
	dib=int(input("Presione 1 para crear un triangulo. \nPresione 2 para crear un cuadrado."))
	if dib==1:
		base=int(input("Ingrese la magnitud de la base del triangulo: "))
		altura=int(input("Ingese la magnitud de la altura del triangulo: "))
		mi_trangulo=Triangulo(base, altura)
		cont="si"
		while cont=="si":
			tri=int(input("Si desea imprimir la imagen presione 1. \nSi desea calcular el area presione 2. "))
			if tri==1:
				print(mi_trangulo.imprimir())
			elif tri==2:
				print("\nEl area del triangulo es: ", mi_trangulo.calcular_area())
			cont=input("Desea continuar?")	
	if dib==2:
		lado=int(input("Ingrese la magnitud del lado del cuadrado: "))
		cont="si"
		mi_cuadrado=Cuadrado(lado)
		while cont=="si":
			cua=int(input("Si desea imprimir la imagen presione 1. \nSi desea calcular el area presione 2."))
			if cua==1:
				print (mi_cuadrado.imprimir())
			elif cua==2:	
				print ("\nEl area del cuadrado es: ",mi_cuadrado.calcular_area())
			cont=input("Desea continuar?")	
	opc=int(input("Presione 1 para crear figura. \nPresione 2 para salir." ))	



