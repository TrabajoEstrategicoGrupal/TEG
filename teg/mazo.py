from paises import *
from random import *

class Tarjeta(object):
        """Implementacion de una tarjeta de pais."""

        def __init__(self, pais, tipo):
                """Constructor desde pais y tipo."""
                self.pais = pais
                self.tipo = tipo

        def __str__(self):
                """Representacion grafica."""
                return "(%s, %s)" % (self.pais, NOMBRE_TARJETAS[self.tipo])

class Mazo(object):
        """Implementacion del mazo de tarjetas de pais."""

        def __init__(self, paises_por_tarjeta):
                """Creacion desde un diccionario de paises segun tipo.
                Debe inicializar el mazo con todas las tarjetas mezcladas."""
                self.mazo=[]
                self.devueltas=[]
                for tipo in paises_por_tarjeta:
                        for pais in paises_por_tarjeta[tipo]:
                                self.mazo.append(Tarjeta(pais,tipo))
                self._barajar()   
                        
        def sacar_tarjeta(self):
                """Saca una tarjeta del mazo.
                Si el mazo se acabara, debe mezclar y empezar a repartir desde
                las tarjetas ya devueltas."""
                if self.mazo==[]:
                        self.mazo=self.devueltas
                        self.devueltas=[]
                        self._barajar()
                return self.mazo.pop()

        def devolver_tarjeta(self, tarjeta):
                """Recibe una tarjeta y la guarda en el pilon de tarjetas
                devueltas. Cuando se acaben las tarjetas del mazo, se mezclaran
                las ya devueltas."""
                self.devueltas.append(tarjeta)

        def cantidad_tarjetas(self):
                """Devuelve la cantidad *total* de tarjetas (tanto en el mazo
                como devueltas)."""
                return (len(self.mazo)+len(self.devueltas))
        
        def _barajar(self):
                l=[]
                for n in xrange(len(self.mazo)):
                        l.append(self.mazo.pop(randrange(len(self.mazo))))
                self.mazo=l
                
        

