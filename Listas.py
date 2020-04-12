lista = [10, True, "cadena de texto", [1,2, "cadena de texto en una lista anidada"]]

elementoSeleccionado = lista[2]

#print(elementoSeleccionado)

elementoSeleccionado = lista[3][2]

#print(elementoSeleccionado)

lista[0]=50

elementoSeleccionado= lista[3]
#print(elementoSeleccionado)

elementosSeleccionados = lista[0:2]

#print(elementosSeleccionados)
#PARTICIONADO o SLICING
elementosSeleccionados = lista[3][0:2]

#print(elementosSeleccionados)

lista = [10, True, "cadena de texto", [1,2, "cadena de texto en una lista anidada"]]

elementosSeleccionados = lista[-2]
#print(elementosSeleccionados)

elementosSeleccionados = lista[1:]
print(elementosSeleccionados)




