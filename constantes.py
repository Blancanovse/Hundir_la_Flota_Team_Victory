## Aspecto tablero
disparo_fallado = "-"
disparo_acertado = "*"
mar = " "



regla_juego = """En este juego, jugarás contra la máquina. Cada uno disparará a una coordenada.
Si se logra disparar en una posición de un barco del adversario, aparecerá una 'X' en el tablero del 
adversario y se podrá seguir disparando mientras se acierta. Si se dispará al agua, apracerá un '-' en 
eltablero del adversario y cambia el turno de disparar. Para ganar, se tiene que disapara a cada posición del adversario."""

# Definir los barcos con sus respectivas longitudes
barcos = {         "barco1": 1, 
                   "barco2": 1, 
                   "barco3": 1, 
                   "barco4": 1, 
                   "barco5": 2, 
                   "barco6": 2, 
                   "barco7": 2, 
                   "barco8": 3, 
                   "barco9": 3, 
                   "barco10": 4}