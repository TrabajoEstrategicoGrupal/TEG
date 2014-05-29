# -*- coding: cp1252 -*-

from dados import *
from mazo import *
from paises import *
from tablero import *

def correr_prueba(caso_prueba, descripcion, resultados_pruebas):
    ''' Comprueba la igualdad pasada por parámetro como caso_prueba y 
    muesta la descripción y su resultado en pantalla. 
    Si no se cumple la igualdad se suma uno a la clave correspondiente en el 
    diccionario resultados_pruebas.
        caso_prueba es una igualdad a la que se le va a aplicar assert.
    descripcion es un texto descriptivo con el que se va a imprimir el 
    resultado de la operación.
    resultados_pruebas es un diccionario con las claves "OK" y "ERROR", que
    identifican valores numéricos con la cantidad de pruebas pasadas y 
    falladas, respectivamente.
    '''
    try:
        assert caso_prueba
        print "Prueba %s: OK" % descripcion
        resultados_pruebas["OK"] += 1
    except AssertionError:
        print "Prueba %s: ERROR" % descripcion
        resultados_pruebas["ERROR"] += 1
    

def prueba_dados(resultados_pruebas):

    dados = Dados()
    print ""
    print "Prueba Dados"
    print ""
    descripcion = "Atacan 100 ejerecitos defienden 30, la cantidad de ejercitos perdidos debe ser 3: "
    dados.lanzar_dados(100,30)
    res_esperado = "3"
    res_real = str(dados.ejercitos_perdidos_atacante()+dados.ejercitos_perdidos_atacado())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Atacan 1 ejerecitos defienden 3, la cantidad de ejercitos perdidos debe ser 0: "
    dados.lanzar_dados(1,3)
    res_esperado = "0"
    res_real = str(dados.ejercitos_perdidos_atacante()+dados.ejercitos_perdidos_atacado())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Atacan 3 ejerecitos defienden 100, la cantidad de ejercitos perdidos debe ser 2: "
    dados.lanzar_dados(3,100)
    res_esperado = "2"
    res_real = str(dados.ejercitos_perdidos_atacante()+dados.ejercitos_perdidos_atacado())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Atacan 1000 ejerecitos defienden 1, la cantidad de ejercitos perdidos debe ser 1: "
    dados.lanzar_dados(1000,1)
    res_esperado = "1"
    res_real = str(dados.ejercitos_perdidos_atacante()+dados.ejercitos_perdidos_atacado())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)


def prueba_mazo(resultados_pruebas):
    mazo = Mazo(paises_por_tarjeta)
    print ""
    print "Prueba Mazo"
    print ""
    descripcion = "Inicializo el mazo y lo barajo, la cantidad de cartas en el mazo son 50: "
    res_esperado = "50"
    res_real = str(mazo.cantidad_tarjetas())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Saca 25 tarjetas del mazo sin devolverlas, la cantidad de cartas en el mazo son 25: "
    for x in xrange(25):
        mazo.sacar_tarjeta()
    res_esperado = "25"
    res_real = str(mazo.cantidad_tarjetas())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Saca 24 tarjetas del mazo y las devuelve, la cantidad de cartas total siguen siendo 25: "
    for x in xrange(24):
        tarjeta=mazo.sacar_tarjeta()
        mazo.devolver_tarjeta(tarjeta)
    res_esperado = "25"
    res_real = str(mazo.cantidad_tarjetas())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Saca 4 tarjetas mas del mazo sin devolverla, el pilon de las cartas devueltas es barajado y puesto en el mazo. La cantidad de cartas en el mazo son 21: "
    for x in xrange(4):
        mazo.sacar_tarjeta()
    res_esperado = "21"
    res_real = str(mazo.cantidad_tarjetas())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

def prueba_tablero(resultados_pruebas):
    t = Tablero(paises_por_continente,paises_limitrofes)
    print ""
    print "Prueba Tablero"
    print ""
    descripcion = "Inicializo el Tablero, todos los paises tienen 1 ejercito : "
    res_esperado =  "1"
    res_real = str(t.ejercitos_pais("Argentina"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Los paises no tienen color: "
    res_esperado = "None"
    res_real = str(t.color_pais("Argentina"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "El negro ocupa argentina con 3 fichas, la cantidad de ejercitos en el pais son 3: "
    t.ocupar_pais("Argentina", NOMBRE_COLORES[COLOR_NEGRO], 3)
    res_esperado = "3"
    res_real = str(t.ejercitos_pais("Argentina"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "El color de argentina es negro: "
    res_esperado = NOMBRE_COLORES[COLOR_NEGRO]
    res_real = t.color_pais("Argentina")
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Se asignan 5 ejercitos a la argentina, la cantidad de ejercitos en el pais son 5: "
    t.asignar_ejercitos( "Argentina", 5)
    res_esperado = "5"
    res_real = str(t.ejercitos_pais("Argentina"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Argentina es limitrofe con Brasil: "
    res_esperado = "True"
    res_real = str(t.es_limitrofe("Argentina","Brasil"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Argentina es limitrofe con Chile: "
    res_esperado = "True"
    res_real = str(t.es_limitrofe("Argentina","Chile"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)
    
    descripcion = "Argentina es limitrofe con Peru: "
    res_esperado = "True"
    res_real = str(t.es_limitrofe("Argentina","Peru"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Argentina es limitrofe con Uruguay: "
    res_esperado = "True"
    res_real = str(t.es_limitrofe("Argentina","Uruguay"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Argentina no es limitrofe con Australia: "
    res_esperado = "False"
    res_real = str(t.es_limitrofe("Argentina","Australia"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)
    
    descripcion = "La cantidad de paises son 50: "
    res_esperado = "50"
    res_real = str(t.cantidad_paises())
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "La cantidad de paises en america del sur son 6: "
    res_esperado = "6"
    res_real = str(t.cantidad_paises_continente('America del Sur'))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "El continente de argentina es America del sur: "
    res_esperado ="America del Sur"
    res_real = str(t.continente_pais("Argentina"))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

    descripcion = "Devuelve la lista con paises de color negro (Argentina): "
    res_esperado = str(['Argentina'])
    res_real = str(t.paises_color(NOMBRE_COLORES[COLOR_NEGRO]))
    correr_prueba(set(res_esperado) == set(res_real), descripcion, resultados_pruebas)

   
    

def correr_pruebas():
    ''' Ejecuta las pruebas y muestra el resultado de toda la ejecución en
    pantalla.
    '''
    resultados_pruebas = { "OK" : 0, "ERROR" : 0 }
    
    prueba_dados(resultados_pruebas)
    prueba_mazo(resultados_pruebas)
    prueba_tablero(resultados_pruebas)
    print ""
    print "Pruebas corridas: %d OK, %d errores." % \
            (resultados_pruebas["OK"], resultados_pruebas["ERROR"]) 
        

correr_pruebas()
