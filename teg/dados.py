from constantes import *
from random import *
CANTIDAD_MAXIMA_DE_LANZAMIENTOS=3
class Dados(object):
      """Implementa la logica de tirar los dados."""

      def __init__(self):
            """Inicializacion del objeto."""
            self._ejercitos_perdidos_atacante = 0
            self._ejercitos_perdidos_atacado = 0
            self._lista_dados = []

      def __str__(self):
            """Representacion de la configuracion de dados de la ultima
            tirada."""
            return "Dados atacantes: "+ str(self._lista_dados[0]) + ", Dados atacados: " + str(self._lista_dados[1]) 


      def lanzar_dados(self, ejercitos_atacante, ejercitos_atacado):
            """Recibe la cantidad de ejercitos presentes en el pais
            atacante y en el pais atacado. Realiza la tirada de los dados.
            El pais que ataca tiene que tener al menos dos ejercitos.
            El pais que ataca ataca con hasta un dado menos que los
            ejercitos que posee, mientras que el pais que defiende lo
            hace hasta con tantos dados como ejercitos.
            La cantidad maxima de dados con la que un pais ataca o defiende
            es siempre 3.
            Cada jugador tira sus dados.
            Los mismos se ordenan de mayor a menor.
            Si un jugador tiro mas dados que otro, los de menor valor se
            descartan.
            Se comparan uno a uno los dados ordenados.
            Cuando el valor de un dado atacante fuera *mayor* que el del
            atacado, el atacado pierde un ejercito. Si no, el atacante lo
            pierde.
            (Leer el reglamento del juego.)"""
            self._reiniciar_ejercitos()
            dados_atacantes = []
            dados_atacados = []
            for x in xrange(CANTIDAD_MAXIMA_DE_LANZAMIENTOS):
                  if(ejercitos_atacante > x+1):
                        dados_atacantes.append(self._tirar_dado())
                  if(ejercitos_atacado > x):
                        dados_atacados.append(self._tirar_dado())
            self._ordenar_lanzamientos_dados((dados_atacantes,dados_atacados))
            for x in xrange(CANTIDAD_MAXIMA_DE_LANZAMIENTOS):
                  try:
                        if(dados_atacantes[x] > dados_atacados[x]):
                              self._ejercitos_perdidos_atacado +=1
                        else:
                              self._ejercitos_perdidos_atacante += 1
                  except:
                        break


      def ejercitos_perdidos_atacante(self):
            """Devuelve la cantidad de ejercitos que perdio el atacante en
            la ultima tirada de dados."""
            return self._ejercitos_perdidos_atacante

      def ejercitos_perdidos_atacado(self):
            """Devuelve la cantidad de ejercitos que perdio el atacado en
            la ultima tirada de dados."""
            return self._ejercitos_perdidos_atacado
      
      def _tirar_dado(self):
            return randint(1,6)#Dado puede devolver enteros de 1 a 6
      
      def _reiniciar_ejercitos(self):
            """Reinicia el conteo de ejercitos perdidos para una nueva tirada"""
            self._ejercitos_perdidos_atacante = 0
            self._ejercitos_perdidos_atacado = 0
            self._lista_dados=[]
            return
                  
      def _ordenar_lanzamientos_dados(self,l_lanzamientos):
            """Recibe una tupla con los lanzamientos del atacante y del atacado
             ordena cada uno de mayor a menor y los agrega a la lista de dados"""
            for lanzamiento in l_lanzamientos:
                  lanzamiento.sort()
                  lanzamiento.reverse()
                  self._lista_dados.append(lanzamiento)
            return
      


	

