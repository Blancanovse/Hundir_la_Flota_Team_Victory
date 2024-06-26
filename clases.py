class Tablero:
    filas = 10
    columnas = 10
    tablero_j01_barcos = np.full((10,10)," ")
    tablero_j01_nada = np.full((10,10)," ")
    tablero_j02_barcos = np.full((10,10)," ")
    tablero_j02_nada = np.full((10,10)," ")

    def __init__(self, jugador01, jugador02):
        self.jugador01 = jugador01
        self.jugador02 = jugador02