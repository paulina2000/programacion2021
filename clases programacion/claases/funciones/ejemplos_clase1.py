
def lineDesign(cantidad,patron ):
    print(patron*cantidad)
    return None

lineDesign (59,'$')
lineDesign (10,'&')
lineDesign (55,'!')

#---Muestre la lista---#
def mostrarLista(listaEntrada):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista= [233,44,937,9838,8,98,234]
lista2= [383,836,34,780,753,85,9]
lineDesign(50,'$')
mostrarLista(lista)
lineDesign(50,'$')
mostrarLista(lista2)

#---Sumar dos numeros---#
def sumar (a=7, b=6):
    sumar = a+b
    return sumar
lineDesign(10, '&')
resultado= sumar()
print(resultado)
print (sumar(35,65))

lineDesign(10, '&')
#---multiplicar dos numeros---#
def multiplicar (a=0, b=0):
    multiplica = a*b
    return multiplica

#---divir dos numeros---#
def dividir (a=0, b=1):
    dividir = a/b
    return dividir

#---potenciar dos numeros---#
def potenciar (base= 5, exponente=2):
    potencia = base ** exponente
    return potencia


#---Funciones dependientes de otras---#
def calcular (operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))

print (multiplicar(76,9))
lineDesign(10, '&')
print (dividir(28,2))
lineDesign(10, '&')
print (sumar(54,6))
lineDesign(10, '&')
print (potenciar(9,4))

calcular(multiplicar,9,3)
