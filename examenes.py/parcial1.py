#---1 calculadora de 3 numeros---#
#---Suma---#
def sumar (a=1, b=3, c=9):
    sumar = a + b + c
    return sumar

print(30*'$')
#---Resta---#
def resta (a=50, b=3, c=7):
    resta = a - b -c
    return resta

print(30*'$')
#---Multiplicacion---#
def multiplicar (a=6, b=2, c=9):
    multiplicar = a * b * c
    return multiplicar

print(30*'$')
#---division---#
def dividir (a=30, b=2, c=3):
    dividir = a / b / c
    return dividir

#---potenciacion---#
def potenciar (base=30, b=2, c=3):
    potenciar = base ** b ** c
    return potenciar


print (sumar(30,20,7))
print(30*'$')
print (resta(60,27,9))
print(30*'$')
print(multiplicar())
print(30*'$')
print(dividir(50,3,2))
print(30*'$')
print (potenciar(2,2,1))

#---2 mostrar 3 listas del mismo tamaño---#
def mostrarLista(listas):
    for elemento in listas:
        print(elemento)
    return None
ingredientes= ['harina', 'chocolate', 'pan', 'huevos', 'azucar', 'vainilla']
utilesAseo= ['jabon', 'shampoo', 'seda dental', 'limpiador facial', 'desodorante', 'perfume']
compras= ['camiseta', 'jean' 'tenis', 'collar','pañoleta', 'aretes']
print(30*'$')
mostrarLista (ingredientes)
print(30*'$')
mostrarLista (utilesAseo)
print(30*'$')
mostrarLista (compras)

print(30*'$')
#---3 area de un triangulo---#

def areaTriangulo (base=10, altura=8):
    area = base * (altura/2)
    return area
area= areaTriangulo (50,10)
print(area)

print(30*'$')
#---4 promedio, maximo y minimos de una lista---#

listaTemp= [33,25,26,31,38,28,39,37,33,37,26,31,29,36,35]
def lista():
    print ('la mayor temperatura es  : ', sum(listaTemp)/len(listaTemp))
    print('la mayor temperatura es el : ', max (listaTemp))
    print('la menor temperatura es el : ', min (listaTemp))
lista()

print(30*'$')
#---5 fibonacci---#
posicion = int(input('posicion de cada numero en el patron : '))
def fibonacci (n):
    if n < 2:
        return n
    else:
        print((n-1)+(n-2))

fibonacci (posicion)
print(30*'$')








