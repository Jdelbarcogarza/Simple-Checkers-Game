import random
from random import randrange


def crear_tablero():
    
    tablero = [["*","_","X","X","_","*"],
               ["_","_","_","_","_","_"],
               ["_","_","_","_","_","_"],
               ["_","_","_","_","_","_"],
               ["_","_","_","_","_","_"],
               ["*","_","E","E","_","*"]
               ]
    
    tablero[randrange(1,5)][randrange(1,5)] = '*'
    tablero[randrange(1,5)][randrange(1,5)] = '*'
    
    
    return tablero
        
def imprimir_tablero(tablero):
    
    for num_col in range(len(tablero)):
        print(f'  {num_col}', end="")
    print()
    
    
    for num_row in range(len(tablero)):
        print(f'{num_row}', end="")
        for element in tablero[num_row]:
            print(f' {element} ',end="")
        print()
    print()
    #esta funcion es la clave, nomas se deben de agregar condicionales
    #y poner lo de saltar al jugador. El problema es que como los dos jugadores entran
    #en una misma variable, no encuentro como revisar si va a saltar o no.
def mover_ficha(renglon, columna, movimiento, tablero, jugador, rival):
    
    nuevo_tablero = tablero
    #movimiento para arriba
    if(movimiento == 'w' and renglon > 0 and nuevo_tablero[renglon-1][columna] != '*' and nuevo_tablero[renglon-1][columna] != rival):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon-1][columna] = jugador
    elif(movimiento == 'w' and nuevo_tablero[renglon-1][columna] == rival and nuevo_tablero[renglon-2][columna] == "_"):   
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon-2][columna] = jugador
        
    #movimiento a la izquierda
    if(movimiento == 'a' and columna > 0 and nuevo_tablero[renglon][columna-1] != '*' and nuevo_tablero[renglon][columna-1] != rival):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon][columna-1] = jugador
    elif(movimiento == 'a' and nuevo_tablero[renglon][columna-1] == rival and nuevo_tablero[renglon][columna-2] == "_"):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon][columna-2] = jugador
        
    #movimiento a la derecha
    if(movimiento == 'd' and columna < 5 and nuevo_tablero[renglon][columna+1] != '*' and nuevo_tablero[renglon][columna+1] != rival):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon][columna+1] = jugador
    elif(movimiento == 'd' and nuevo_tablero[renglon][columna+1] == rival and nuevo_tablero[renglon][columna+2] == "_"):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon][columna+2] = jugador
        
    #movimiento hacia abajo   
    if(movimiento == 's' and renglon < 5 and nuevo_tablero[renglon+1][columna] != '*' and nuevo_tablero[renglon-1][columna] != rival):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon+1][columna] = jugador
    elif(movimiento == 's' and nuevo_tablero[renglon+1][columna] == rival and nuevo_tablero[renglon+2][columna] == "_"):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon+2][columna] = jugador
    
    else:
        
        print("Turno perdido")

    return nuevo_tablero
    
    
def turno(jugador, tablero, rival):
    
    renglon = int(input("Selecciona el renglon de la ficha a mover: "))
    
    while(renglon < 0 or renglon > 5):
        
        print("Por favor escribe un renglón válido")
        renglon = int(input())
        
    columna = int(input("Selecciona la columna de la ficha a mover: "))
    
    while(columna < 0 or columna > 5):
        
        print("Por favor escribe una columna válida")
        columna = int(input())

    movimiento = input("Dirección a mover? 'w' arriba, 'a' izquierda, 'd' derecha, 's' abajo: ")
    
    while (movimiento != 'w' and movimiento != 'a' and movimiento != 'd' and movimiento != 's'):
        
        print("No existe esa dirección")
        movimiento = input("Escribe una dirección válida: ")
     
    if(tablero[renglon][columna] == "_"):
        print("Pierde turno")
    else:
        
        tablero = mover_ficha(renglon, columna, movimiento, tablero, jugador, rival)
        return tablero
    
def main():
    
    jugador_E = 'E'
    jugador_X = 'X'
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    run = 's'
    
    while(run == 's'):
        
        print(f'Turno jugador {jugador_E}')
        turno(jugador_E, tablero, jugador_X)
        imprimir_tablero(tablero)
        
        
          
        run = input("Quieres seguir jugando s/n? ")
        
        if(run != 's'):
            break
        
        print(f'Turno jugador {jugador_X}')
        turno(jugador_X, tablero, jugador_E)
        imprimir_tablero(tablero)
    
main()