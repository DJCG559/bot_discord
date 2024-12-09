import random 

def gen_juego():

    #lista de juegos

    list_juego = ["FIFA","FORTNITE","CALL OF DUTY","MINECRAFT","OVERWATCH","F1","ROCKET LEAGE","MORTAL COMBAT"]

    #seleccion de un juego aleatorio

    juego_elegido = random.choice(list_juego)

    return juego_elegido

