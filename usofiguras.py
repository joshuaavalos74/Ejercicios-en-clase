from cuadrado import Cuadrado
from triangulo import Triangulo
mi_trangulo=0
mi_cuadrado=0
print("Bienvenido a el creador de cuadrados, triangulos y calculador de sus areas. De Naruto.")
opc=int(input("Presione 1 para crear figura. \n Presione 2 para salir."))
while opc==1:
	dib=int(input("Presione 1 para crear un triangulo. \n Presione 2 para crear un cuadrado."))
	if dib==1:
		base=int(input("Ingrese la magnitud de la base del triangulo: "))
		altura=int(input("Ingese la magnitud de la altura del triangulo: "))
		mi_trangulo=Triangulo(base, altura)
		print(mi_trangulo.imprimir())
		print("El area del triangulo es: ", mi_trangulo.calcular_area())
	if dib==2:
		lado=int(input("Ingrese la magnitud del lado del cuadrado: "))
		mi_cuadrado=Cuadrado(lado)
		print (mi_cuadrado.imprimir())
		print (mi_cuadrado.calcular_area())
	opc=int(input("Presione 1 para crear figura. \n Presione 2 para salir." ))	



