from abstraccion import * 

""" creamos dos jugadores
 
"""
def comprobar(num,num2):
    if num > 0 and num2 > 0 :
        return True 
    else:
        return False
        # comment: 
def juego():
    """
    Purpose: 

    """
    turno = 0
    jugador = Jugador("Save") 
    jugador2 = Jugador("Contrincante")
    """so a los jugadores les queda hp o cartas en el mazo 
        pasa al siguiente turno
    """
    while comprobar(jugador.hp,jugador2.hp) or comprobar(len(jugador.mazo),len(jugador2.mazo)) :
        turno = +1 

        print(f" turno # {turno} ")
        print(f" {jugador.nombre} {jugador.hp} HP")
# end def



