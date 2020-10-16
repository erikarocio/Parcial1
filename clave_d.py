import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(numero1, numero2, numero3):
    return numero1 * numero2 * numero3



"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    result = sum([i for i in range(1000, 2001) if i % 5 == 0 and i % 3 == 0])
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(longitud, latitud, altura):
    result1 = obtenerArea(longitud, latitud, altura)
    result2 = obtenerVolumen(longitud, latitud, altura)
    result = {"area" : result1, "volumen": result2}
    return result


def obtenerArea(valorlongitud, valorlatitud, valoraltura):
    area = 2 * valorlongitud * (valorlatitud + valorlongitud) * (valoraltura + valorlatitud) * valoraltura
    result = area
    return result


def obtenerVolumen(valorlongitud, valorlatitud, valoraltura):
    volumen = valorlongitud * valorlatitud * valoraltura
    result = volumen
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def __init__(self, longitud, latitud, altura):
        self.longitud = longitud
        self.latitud = latitud
        self.altura = altura

    def definicionOrtoedro(self, longitud, latitud, altura):

    

        return 0


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
