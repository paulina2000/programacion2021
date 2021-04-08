#---Sumar dos numeros---#
def sumar (a=7, b=6):
    sumar = a+b
    return sumar

lineDesign(10, '&')
#---multiplicar dos numeros---#
def multiplicar (a=0, b=0):
    multiplica = a*b
    return multiplica

lineDesign(10, '&')
#---divir dos numeros---#
def dividir (a=0, b=1):
    dividir = a/b
    return dividir

lineDesign(10, '&')
#---potenciar dos numeros---#
def potenciar (base= 5, exponente=2):
    potencia = base ** exponente
    return potencia

#---Funciones dependientes de otras---#
def calcular (operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))