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
    
def mover_ficha(renglon, columna, movimiento, tablero):
    
    nuevo_tablero = tablero
    if(movimiento == 'w'):
        nuevo_tablero[renglon][columna] = '_'
        nuevo_tablero[renglon+1][columna] = 
    
    
    return nuevo_tablero
    
def main():

    jugador_E = 'E'
    jugador_X = 'X'
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    empieza = randrange(0,2)
    
    
    if(empieza == 1):
        print(f'Comienza jugador {jugador_E}')
    else:
        print(f'Comienza jugador {jugador_X}')
    
    
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
        
    tablero = mover_ficha(renglon, columna, movimiento, tablero)
    imprimir_tablero(tablero)
    
main()