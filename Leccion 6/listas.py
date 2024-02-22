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
# print(frutas)

# #saber largo de tupla
# print(len(frutas))

# #acceder a elemento
# print(frutas[0])

# #navegacion inversa
# print(frutas[-1])

# #acceder a un rango
# print(frutas[0:2])

#recorrer elementos

# for fruta in frutas:
#     print(fruta, end=' ')

#cambiar valor de tupla

# frutas[0] = 'pera'

# frutaLista = list(frutas)
# frutaLista[0] = 'Pera'
# frutas = tuple(frutaLista)
# print('\n',frutas)

# #eliminar tupla

# del frutas
# print(frutas)

#Dada la siguiente tupla, crear lista que solo incluya
#los numeros menores a 5

# tupla = (13, 1, 8, 3, 2, 5, 8)

# # tuplaLista = list(tupla)

# # for i in tuplaLista:
# #     if i < 5:
# #         print(i)

# #el mismo ejercicio
        
# #definir lista        
# lista = []
# #filtrar elementos mejores a 5 de la tupla
# for elemento in tupla:
#     if elemento <5:
#         lista.append(elemento)
# print(lista)

#coleccion set 
#no mantiene orden ni elementos duplicados, ni modificar
#es posible agregar y eliminar elementos

# planetas = {'Marte', 'jupiter','Venus'}

# print(planetas)

# #largo del set

# print(len(planetas))

# #revisar si un elemento esta presente
# print('Marte' in planetas)

# #agregar elementp
# planetas.add('Tierra')
# print(planetas)

# #eliminar elemento
# planetas.remove('Tierra')

# planetas.discard('Jupiter') #no arroja error al no encontrar elemento

# #limpiar set

# planetas.clear()

# #eliminar set
# del planetas


#diccionarios (KEY,VALUE)

diccionario = {
    'IDE': 'Integred development environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

#tamaño del diccionario
print(len(diccionario))

#acceder a un elemento del diccionario
print(diccionario['IDE'])
#otra forma de acceder
print(diccionario.get('OOP'))
#modificar elementos
diccionario['IDE']= 'idee'
print(diccionario)

#recorrer elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprabar existencia de elemento en diccionario
    
print('IDE'in diccionario)

#agregar elemento

diccionario['PK'] = 'Primary key'
print(diccionario)

#remover elemenento
diccionario.pop('IDE')

#limpiar
diccionario.clear()

#eliminar diccionario
del diccionario