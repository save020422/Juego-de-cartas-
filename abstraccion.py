
class Carta:
    def __init__(self,nombre,coste_mana,tipo):
        self.nombre = nombre 
        self.coste_mana = coste_mana
        self.tipo = tipo 

        def usar(self,jugador):
           if not self.tipo == "habilidad":
                  print(f" la carta de habilidad {self.nombre} a sido activada")
           else:
                print(f" La leyenda {self.nombre} a sido llamada al campo")

class Leyenda(Carta):
     def __init__(self, nombre, coste_mana, pa , pi,tipo,):
          super().__init__(nombre, coste_mana, "Leyenda")
          self.nombre = nombre 
          self.pa = pa 
          self.pi = pi
     def atacar():
        pass
        """
        Purpose: 
        """

        
    # end def
            
class Jugador:
     def __init__(self,nombre):
          self.nombre = nombre 
          self.hp = 20
          self.mana = 1
          self.mazo =[]
          self.mano =[]
          self.campo =[]
          self.vacio =[]
          
          
     def robar(self):
          carta_r = self.mazo.pop
          self.mano.append(carta_r)

          print(f"{self.nombre} robaste una carta")
     def usar_carta(self):
          carta_us = self.mazo.pop
          ''' en un futuro implementar
                una condicion
                que limite el uso de cierta 
                cantidad de cartas
          '''
          self.campo.append(carta_us)
          

