# listas 

nombre = ['Juan', 'carlos', 'choro', 'laji']
# print(nombre)
# #acceder a elementos de manera individual
# print(nombre[0])
# #acceder de manera inversa
# print(nombre[-1])
# #imprimir rango
# print(nombre[0:2])#sin incliur indice
# #desde inicio de lista hasta indice (sin incluir)
# print(nombre[:3])
# #desde el indice indicado hasta el final
# print(nombre[1:])

# #cambiar valor de lista
# nombre[1]='maldito'
# print(nombre)

#iterar lista

# for nombres in nombre:
#     print(nombres)
# else:
#     print(f'no existen mas nombres en la lista')

# #consultar largo de una lista
# print(len(nombre))

# #agregar elementos
# nombre.append('Chuchetumare')
# print(nombre)

# #agregar elemento en indice especifico
# nombre.insert(1, 'Octavio')
# print(nombre)

# #remover elemento
# nombre.remove('carlos')
# print(nombre)

# #remover ultimo valor agregado
# nombre.pop()
# print(nombre)

# #eliminar un indice
# del nombre[0]
# print (nombre)

# #limpiar lista
# nombre.clear()
# print(nombre)

# #eliminar lista (variable nombre)
# del nombre
# print(nombre)

#Tupla ,tipo inmutable

frutas = ('manzana', 'naranja', 'platano')
print(frutas)

#saber largo de tupla
print(len(frutas))

#acceder a elemento
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#acceder a un rango
print(frutas[0:2])