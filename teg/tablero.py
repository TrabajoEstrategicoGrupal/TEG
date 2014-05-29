from paises import *
from constantes import *
from interfaz import Interfaz

class Pais(object):
        """Clase que representa cada pais del juego"""
        def __init__(self,continente,limitrofes,ejercitos=1,color=None):
                self.color=color
                self.continente=continente
                self.limitrofes=limitrofes
                self.ejercitos=ejercitos
        def __str__(self):
                return str(self.color)+" "+str(self.continente)+" "+str(self.limitrofes)+" "+str(self.ejercitos)
                
class Tablero(object):
        """Clase que representa el tablero de juego."""

        def __init__(self, continentes, limitrofes):
                """Crea un tablero desde un diccionario de continentes con su
                lista de paises, y un diccionario de paises y su lista de
                limitrofes."""
                self.paises={}
                for cont in continentes:
                        for pais in continentes[cont]:
                                self.paises[pais]=(Pais(cont,limitrofes[pais]))

        def ocupar_pais(self, pais, color, ejercitos=1):
                """Ocupa el pais indicado con ejercitos del color."""
                self.paises[pais].color=color
                self.paises[pais].ejercitos=ejercitos

        def asignar_ejercitos(self, pais, ejercitos):
                """Suma o resta una cantidad de ejercitos en el pais indicado."""
                self.paises[pais].ejercitos=ejercitos

        def actualizar_interfaz(self, agregados=None):
                """Redibuja interfaz grafica. Puede recibir un diccionario de
                paises y numero de ejercitos que se adicionan o sustraen a los
                que estan ubicados en el tablero.
                Por ejemplo, si el diccionario fuera
                {'Argentina': -1, 'Brasil': 1}, el tablero se dibujaria con un
                ejercito menos en Argentina y uno mas en Brasil."""
                dicc_ejercitos={}
                if agregados:
                        for pais in agregados:
                                dicc_ejercitos[pais]=(self.paises[pais].color, self.paises[pais].ejercitos+agregados[pais])
                Interfaz.ubicar_ejercitos(dicc_ejercitos)
                # Utilizar la funcion de la Interfaz, que recibe un diccionario
                # de paises y colores, por ejemplo:
                # >>> paises = {'Argentina': (COLOR_NEGRO, 10), 'Brasil':
                # ...   (COLOR_ROSA, 1)}
                # >>> Interfaz.ubicar_ejercitos(paises)
                # Va a poner 10 ejercitos negros en Argentina y 1 rosa en
                # Brasil.

        def color_pais(self, pais):
                """Devuelve el color de un pais."""
                return self.paises[pais].color

        def ejercitos_pais(self, pais):
                """Devuelve la cantidad ejercitos en un pais."""
                return self.paises[pais].ejercitos

        def es_limitrofe(self, pais1, pais2):
                """Informa si dos paises son limitrofes."""
                return (pais2 in self.paises[pais1].limitrofes)

        def cantidad_paises(self):
                """Informa la cantidad de paises totales."""
                return len(self.paises)

        def cantidad_paises_continente(self, continente):
                """Informa la cantidad de paises en continente."""
                c=0
                for pais in self.paises:
                        if self.paises[pais].continente==continente:
                                c=c+1
                return c

        def continente_pais(self, pais):
                """Informa el continente de un pais."""
                return self.paises[pais].continente

        def paises_color(self, color):
                """Devuelve la lista de paises con ejercitos del color."""
                l=[]
                for pais in self.paises:
                        if self.paises[pais].color==color:
                                l.append(pais)
                return l
