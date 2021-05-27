import matplotlib.pyplot as plt

#---punto 1---#


PREGUNTA_FAV = 'Cuales son tus 8 alimentos favoritos?  : '
PREGUNTA_PRECIOS = 'Cuales son los precios de esos productos que elejiste? : '
favoritos= []
n=8
while(n>0):
    favorito = input (PREGUNTA_FAV)
    favoritos.append(favorito)
    n= n-1

precios=[]
n=8
while(n>0):
    precio = int (input(PREGUNTA_PRECIOS))
    precios.append(precio)
    n=n-1


#----Grafico de barras----#

plt.bar(favoritos, precios, width= 0.7, color= 'b' )
plt.title('8 Alimentos  favoritos con sus precios')
plt.xlabel('top 8 comida favorita')
plt.ylabel('precios de los alimentos')
plt.savefig ('graficoSnaks.png')

plt.show()


print(60*'*2*')
#---punto2---#
class Humano ():
    def __init__ (self, nameIn, ageIn, sexIn):
        self.name = nameIn
        self.age = ageIn
        self.sex = sexIn
    def hablar (self, mensaje):
        print(f'''Hola mi nombre es {self.name} 
        y tengo {self.age} mi sexo es {self.sex} y 
        ''', mensaje)


humano1 = Humano('laura', 34, 'femenino')
humano1.hablar ('me encanta salir a comer con mis amigos a comer hamburguesa')

print(60*'*2*')
class Doctor (Humano):
    def __init__ (self, nameIn, ageIn, sexIn, pesoIn, alturaIn):
        Humano.__init__(self, nameIn, ageIn, sexIn )
        self.peso = pesoIn
        self.altura = alturaIn
        print(f'Hola me llamo {self.name} tengo {self.age} años soy su Doctor y mi sexo es {self.sex} ')
    def imc (self, pesoIn, alturaIn):
        imc = pesoIn / (alturaIn)**2
        print(f' mi indice de masa corporal es {imc} kilos')

doc1 = Doctor( 'rafael', 24, 'masculino', 60, 1.80)
doc1.imc (70, 1.70)



print(60*'*3*')
IsCorrectInfo = False
while (IsCorrectInfo == False):
    try:
        name = input('Ingresa tu nombre por favor : ')
        assert(name.isalpha())
        IsCorrectInfo = True
    except AssertionError:
        print ('Ingresaste un dato no valido no se admiten numeros en tu nombre')

IsCorrectInfo =False
while (IsCorrectInfo == False):
    try: 
        dolares = float(input('Ingresa el monto de dinero que tienes en dolares : '))
        euros = dolares* 0.82
        print(f' hola mi nombre es {name} y el monto de dolares que tengo convertido a euros es {euros} euros ')
        IsCorrectInfo = True
    except ValueError:
        print('el valor que ingresaste no es valido')







print(60*'*4*')
import sys
nombre = input('ingrese su nombre : ')
enfermedad =  input('ingrese su enfermedad: ')
precio = int (input('cual es el precio de la consulta? : '))

nombreArchivo = 'pacientes.txt'
try:
    archivo = open (nombreArchivo)
    print('1')
except FileNotFoundError:
    archivo=open (nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Archivo de pacientes neurologicos'
    print('2')
    archivo.writelines(descripcion)
    sys.exit(1)

archivo=open(nombreArchivo, 'a')
linea = ' \nnombre: ' + nombre + ' enfermedad: ' + str(enfermedad) + ' precio: ' + str(precio)
archivo.writelines(linea)
archivo.close()
#---Gracias por todo lo que nos enseño este semestre profe, demasiado buen profesor---#