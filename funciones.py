# Empezar a jugar
def empezar_juego():
    pregunta_01 = input("Hola, ¿quieres iniciar un partido?(Contesta por S [sí] o N [no])")

    if pregunta_01 == "S":
        pregunta_02 = input("¿Cuál es tu nombre?")
        Tablero.jugador01 = pregunta_02
        Tablero.jugador02 = "oponente"

        print(regla_juego)

        posicion_barco(Tablero.tablero_j01_barcos, Tablero.filas, Tablero.columnas)
        posicion_barco(Tablero.tablero_j02_barcos, Tablero.filas, Tablero.columnas)
        print("*"*40)
        print("Tablero de", pregunta_02)
        print("*"*40)
        print(Tablero.tablero_j01_barcos)
        print("*"*40)
        print("Tablero del", Tablero.jugador02)
        print("*"*40)
        print(Tablero.tablero_j02_nada)
    else:
        print("¡Hasta luego!")

# Verificación posición de los barcos
def verificar_posicion(tablero, fila, columna, longitud, direccion):
    """Verifica si un barco cabe en la posición dada y no se superpone."""
    if direccion == "H":  # Horizontal
        if columna + longitud > 10:
            return False
        for posicion in range(longitud):
            if tablero[fila, columna + posicion] != " ":
                return False
    else:  # Vertical
        if fila + longitud > 10:
            return False
        for posicion in range(longitud):
            if tablero[fila + posicion, columna] != " ":
                return False
    return True

def colocar_barco(tablero, fila, columna, longitud, direccion):
    """Coloca un barco en el tablero en la posición dada."""
    if direccion == "H":  # Horizontal
        for posicion in range(longitud):
            tablero[fila, columna + posicion] = "O"
    else:  # Vertical
        for posicion in range(longitud):
           tablero[fila + posicion, columna] = "O"

# Colocar los barcos
def posicion_barco(tablero, fila, columna):
    for barco, longitud in barcos.items():
        colocado = False
        while not colocado:
            direccion = random.choice(["H", "V"])
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            if verificar_posicion(tablero, fila, columna, longitud, direccion):
                colocar_barco(tablero, fila, columna, longitud, direccion)
                colocado = True

def verif_disparar():
    fila = int(input("Introduce la fila (0-9) para disparar: "))
    columna = int(input("Introduce la columna (0-9) para disparar: "))
    if fila >= 0 and fila <= 9 and columna >= 0 and columna <= 9:
        coordenadas_disparo = [fila, columna]
        print(coordenadas_disparo)
        print("Coordenas válidas")
    else:
         print("Coordenadas no válidas, intentalo de nuevo")

def disparar(tablero_vacio, tablero_oponente_barcos):
    verif_disparar()
    if tablero_oponente_barcos[coordenadas_disparo] == "0":
        tablero_oponente_barcos[coordenadas_disparo] = "X"
        tablero_vacio[coordenadas_disparo] = "X"
        print("¡Tocado!")
        print(tablero_vacio)
    elif tablero_oponente_barcos[coordenadas_disparo] == "X":
        print("¡Ya has disparado aquí!")
        print(tablero_vacio)
    else:
        tablero_oponente_barcos[coordenadas_disparo] = "-"
        tablero_vacio[coordenadas_disparo] = "-"
        print(tablero_vacio)