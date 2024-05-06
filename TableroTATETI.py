from random import randrange

def display_board(board):                           # Muestra el estado actual del tablero
    i2 = 0
    for i in range(0, 13):
        j2 = 0
        for j in range(0, 25):
            if i%4 == 0:                            # Si fila es -----
                if j%8 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            elif i in (2, 6, 10):                   # Si fila es dato o |
                if j%8 == 0:
                    print("|", end="")
                elif j in (4, 12, 20):              # Si fila y col es dato, copia con indices i2, j2 desde board
                    print(board[i2][j2], end="")
                    j2+=1
                    if j == 20:
                        i2+=1
                else:
                    print(" ", end="")
            else:                                   # Si fila es | o " "
                if j%8 == 0:
                    print("|", end="")
                else:
                    print(" ", end="")
        print(end="\n")


def make_list_of_free_fields(board):                # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    lista_libres = []

    for i in range(0, 3):
        for j in range(0, 3):
            try:
                if board[i][j] in range(1, 10):
                    lista_libres.append((i, j))
            except:
                continue
    return lista_libres


def draw_move(board):                               # Dibuja el movimiento de la máquina y actualiza el tablero
    libres = make_list_of_free_fields(board)
    print("Turno de la computadora")
    while True:
        aleatorio = randrange(10)
        for coordenada in libres:
            i, j = coordenada[0], coordenada[1]
            if aleatorio == board[i][j]:
                board[i][j] = "X"
                return
            


def victory_for(board, sign):               # La función analiza el estatus del tablero para verificar si 
                                            # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][2] == sign:       # Horizontales
        return True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]  and board[1][2] == sign:
        return True
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][2] == sign:
        return True
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[2][0] == sign:     # Verticales
        return True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[2][1] == sign:
        return True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[2][2] == sign:
        return True
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[2][2] == sign:     # Oblicuas
        return True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[2][0] == sign:
        return True
    return False


def enter_move(board):                                  # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    libres = make_list_of_free_fields(board)            # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

    while True:
        try:
            eleccion = int(input("Ingresa tu movimiento: "))
            if eleccion in range(1, 10):
                for coordenada in libres:
                    i, j = coordenada[0], coordenada[1]
                    if board[i][j] == eleccion:
                        board[i][j] = "O"
                        return      
                print("La posicion no está disponible")              
                
            else:
                print("Debes ingresar un número del 1 al 9.")
                        
        except(ValueError):
            print("Debes ingresar un número del 1 al 9.")
        except():
            print("Ingreso incorrecto.")




board = [[1, 2, 3],[4, "X", 6],[7, 8, 9]]
win = False
display_board(board)

for i in range(1, 9):
    if i % 2 == 0:
        draw_move(board)
        if victory_for(board, "X"):
            display_board(board)
            print("¡PERDISTE! ¡La computadora te ganó!")            
            win = True
            break
    else:
        enter_move(board)
        if victory_for(board, "O"):
            display_board(board)
            print("¡GANASTE!")            
            win = True
            break
    display_board(board)
if not win:
    display_board(board)
    print("¡EMPATARON!")

        
