#---1 Dada una lista muestrela en pantalla elemento a elemento#---#
def mostrarLista (lista):
    for elemento in lista:
        print (elemento)

ingredientes = ['chocolate', 'vainilla', 'leche', 'huevos', 'azucar', 'harina']
utiles= ['cuadernos', 'lapiceros', 'regla', 'colores', 'atlas', 'carpetas', 'resaltador']
mostrarLista(ingredientes)
print (30*'$')
mostrarLista(utiles)

#---2 Dada una lista de numeros enteros muestre la en pantalla el numero mas grande---#
#---El mas pequeño y el promedio de la lista---#




print (30*'$')
#---3 Salude n veces---#
def saludos (cantidad=0):
    print ('helloo  ' * cantidad)
saludos (30)


print (30*'$')
#--4 Que devuelva todos los números pares de una lista de números enteros--#
def listaPar(lista):
    par = []
    for elemento in lista:
        if elemento % 2==0 :
            par.append (elemento)
        return par

temperaturas= [25,26,31,38,28,39,37,33,37,26,31,29,36,35]
temperaturasPar = listaPar (temperaturas)
print (temperaturasPar)