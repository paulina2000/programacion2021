#---Funciones sin entrada---#
print('#'*60)
print('#'*60)
def lineDesign():
    print('#'*60)
lineDesign()
print ('hola')
print('como estas?')
lineDesign()

#---Funciones con una entrada---#
def lineDesignC(cantidad):
    print('#'*cantidad)
lineDesignC(1)

#---Funcion suma---#

def sumar (valor1=0, valor2=5):
    return valor1 + valor2
print (sumar (2,2))
print (sumar())

#---Funcion resta---#

def resta (valor1=3, valor2=4):
    return valor1 - valor2
print (resta ())
print (resta (4,6))

#---Funcion multiplicacion---#

def multiplicacion (valor1=9, valor2=6):
    return valor1 * valor2
print (multiplicacion ())
print (multiplicacion (9,17))


#---Funcion division---#

def division (valor1=13, valor2=8):
    return valor1 / valor2
print (division (934,123))
print (division ()) 


#---Funciones que utilizan otras---#

def calculadora (accion, valor1, valor2):
    print (accion (valor1,valor2))
lineDesignC(30)
calculadora (sumar, 3,6)
lineDesignC(30)
calculadora (division, 7,2)
lineDesignC(30)
calculadora (multiplicacion, 4,9)
lineDesignC(30)
calculadora (resta, 20,10)


