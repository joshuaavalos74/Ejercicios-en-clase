from classfigura import FiguraGeometrica
class Cuadrado(FiguraGeometrica)

	def __init__(self, lado):
		super(). __init__(lado, lado)

	def imprimir(self):
		resultado = " "

		for i in range(self.altura):
			resultado += "* " * (i+1) * (self.base) + "\n"

		return resultado	