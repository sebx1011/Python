# Problema

# Piedra, papel o tijeras es un juego infantil, un juego de manos en el que existen tres elementos: la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo y el papel que vence a la piedra envolviéndola, dando lugar a un círculo o ciclo cerrado, que caracteriza al juego. Se utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se hace a veces usando una moneda, o para dirimir algún asunto.

# Deberá recibir la información de las jugadas del usuario mediante input, y deberá indicar que jugador ganó, o si fue un empate.

# Input Format

# Jugada del jugador 1 Jugada del jugador 2

# Constraints

# Solo ingresaran los siguientes inputs:

# Piedra
# Papel
# Tijeras
# Output Format

# Resultados:

# Gano el jugador 1
# Gano el jugador 2
# Empate
# Sample Input 0

# Piedra
# Tijeras
# Sample Output 0

# Gano el jugador 1
# Sample Input 1

# Papel
# Piedra
# Sample Output 1

# Gano el jugador 1
# Sample Input 2

# Tijeras
# Tijeras
# Sample Output 2

# Empate



#Solucion original

jugador1 = str(input(f'Jugada del jugador 1: '))
jugador2 = str(input(f'Jugada del jugador 2: '))

if jugador1 == 'Piedra' and jugador2 == 'Papel':
    print(f'Gano el jugador 2 ')

elif jugador1 == 'Piedra' and jugador2 == 'Tijera':
    print(f'Gano el jugador 1 ')

elif jugador1 == 'Papel' and jugador2 == 'Tijera':
    print(f'Gano el jugador 2 ')

elif jugador1 == 'Papel' and jugador2 == 'Piedra':
    print(f'Gano el jugador 1 ')

elif  jugador1 == 'Tijera' and jugador2 == 'Piedra':
    print(f'Gano el jugador 2 ')

elif jugador1 == 'Tijera' and jugador2 == 'Papel':
    print(f'Gano el jugador 1 ')

else:
    print(f'Empate')

#Solucion aceptada
#solo es espera el input, no los mensajes intermedios para entender el codigo
jugador1 = str(input()).capitalize() #.capitalize() convierte el primer caracter del input en mayuscula y los demas en minuscula
jugador2 = str(input()).capitalize()

if jugador1 == 'Piedra' and jugador2 == 'Papel':
    print(f'Gano el jugador 2')

elif jugador1 == 'Piedra' and jugador2 == 'Tijeras':
    print(f'Gano el jugador 1')

elif jugador1 == 'Papel' and jugador2 == 'Tijeras':
    print(f'Gano el jugador 2')

elif jugador1 == 'Papel' and jugador2 == 'Piedra':
    print(f'Gano el jugador 1')

elif  jugador1 == 'Tijeras' and jugador2 == 'Piedra':
    print(f'Gano el jugador 2')

elif jugador1 == 'Tijeras' and jugador2 == 'Papel':
    print(f'Gano el jugador 1')

else:
    print(f'Empate')