def maximo (lista):
	if len(lista)== 1:
		return lista[0]

	sublista= lista[1:]
	submaximo= maximo(sublista)	

	if lista[0]> submaximo:
		return lista[0]
	return submaximo	