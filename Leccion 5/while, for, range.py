#print ("Hello world")

#ejercicio while

#contador = 0

#while contador < 3:
#    print(contador)
#    contador += 1
#else:
#    print(f'fin del ciclo while')

#ciclo while imprimr numero de 0 a 5
#maximo = int(5)

#contador = int(0)

#while contador <= maximo:
 #   print(contador)
  #  contador +=1
#else:
 #   print(f'fin de ciclo')

#Ciclo while descendente imprimir numero de 5 a 1

#minimo = int (1)
#contador = int (5)
#
#while contador >= minimo:
 #   print(contador)
  #  contador -=1
#else:
 #   print(f'Fin del ciclo')

# ciclo for
    
# cadena = 'hola'

# for letra in cadena:
#     print(letra)
# else:
#     print(f'fin del ciclo')

#break

# for letra in 'holanda':
#     if letra == 'a':
#         print(f'Letra encontrada: {letra}')
#         break
# else:
#    print('Fin ciclo for')

#palabra continue

# for i in range(6):
#     if i % 2 == 0:
#         print(f'valor: {i}')

# for i in range(6):
#     if i % 2 != 0:
#         continue
#     print(f'valor : {i}')


#iterar un rango de 0 a 10 e imrprimir numeros divisibles entre 3
    
# for i in range(11):
#   if i % 3 !=0:
#     continue
#   print(f'valor: {i}')

#crear unm rango de numeros de 2 a 6 e imprimirlos
#los 2 funcan pero de distinta manera  

# for i in range(2,7):
#   print(f'valor: {i}')

# rango = range(2,7)

# for i in rango:
#   print(i)

# #crea un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
#primero nada que ver, no funca
 
# for i in range(3, 10):
#   if i < i+1:
#     print (f'valor: {i}')

rango = range(3,11,2)

for i in rango:
    print(f'valor: {i}')