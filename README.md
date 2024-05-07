<h1 align="center"> Juego TA-TE-TI </h1>

Proyecto del curso de Cisco Python 1.

## :hammer:Enunciado
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

- la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
- el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
- el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
- todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
- el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
- el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
- la maquina responde con su movimiento y se verifica el estado del juego;
- no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

El ejemplo del programa es el siguiente:

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
¡Has Ganado!
```

## 🔧 Tecnologías utilizadas
- Python 3

## 📦 Despliegue
Editor de texto que soporte Python

## :loudspeaker: Solución
Funciones usadas:
- **display_board(board)**
  
    Muestra el estado actual del tablero.
  
- **make_list_of_free_fields(board)**
  
    Examina el tablero y construye una lista de todos los cuadros vacíos. La lista es una lista de tuplas con los índices de filas y columnas.
  
- **draw_move(board)**
  
    Dibuja el movimiento de la máquina y actualiza el tablero.
  
- **victory_for(board, sign)**
  
    Analiza el estado del tablero y verifica si *sign* ("O" o "X") formó línea.

- **Main**

    Dentro de un loop con la cantidad de turnos para que se llene el tablero, pregunta si el índice es par o impar para saber a quién le toca el turno (computadora o jugador).
    Con cada movimiento, pregunta si el último que movió ganó. Si se sale del for, y nadie ganó (win=false) significa que empataron.

## ✒️ Autor
* **Cristian Muñoz** - [crismkle](https://github.com/crismkle)
