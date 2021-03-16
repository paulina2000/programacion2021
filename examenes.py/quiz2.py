

TemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]


#---preguntas---# 
PreguntaNumero = ''' elija entre estas opciones
1. hacer conversion de grados centigrados a kelvin o a fahrenheit
2. Clasificar las temperaturas 
3. temperatura maxima o minima y cada cuanto se tomaba
4. salir 
'''

PreguntaEscalaTemperatura = ''' 
k- Mostrar temperatura en kelvin
F- Mostrar temperatura en fahrenheit
c- Esta conversion no es necesaria 
'''
PreguntaTemperatura = " indique por favor la temperatura del paciente : "

#---conversiones---#

ListaFahrenheit = []
for numero in TemperaturaCorporal:
    conversor = round ((numero * 1.8)+32)
    ListaFahrenheit.append (conversor)
ListaKelvin = []
for numero in TemperaturaCorporal:
    conversor = round(numero + 273.15)
    ListaKelvin.append (conversor)


#---Entrada a el codigo---#

NumeroElejido = int(input(PreguntaNumero))
while (NumeroElejido != 4):
    #----pregunta 1----#
    if (NumeroElejido == 1):
        OpcionEscala = (input(PreguntaEscalaTemperatura))
        if (OpcionEscala == 'K'):
            print('Aqui se muestra la lista en grados kelvin')
            print (ListaKelvin)
        elif(OpcionEscala == 'F'): 
            print('Aqui se muestra la lista en grados fahrenheit')
            print(ListaFahrenheit)
        elif(OpcionEscala == 'C'):
            print('Esta conversion no es necesaria')
            print(TemperaturaCorporal)
        else:
            print('La opcion ingresada no es valida por favor ingrese una opcion valida')
    #----pregunta 2----#
    elif(NumeroElejido ==2):
        Temperatura = float(input(PreguntaTemperatura))
        if(Temperatura < 36):
            print('Quiere una cobija? tiene hipotermia')
            print('Su temperatura es de : ', Temperatura)
        elif(Temperatura >= 36 and Temperatura < 37.5):
            print('Su temperatura es normal')
            print('Su temperatura es de : ', Temperatura)
        else:
            print('Usted tiene una temperatura alta al parecer tiene fiebre')
            print('Su temperatura es de : ', Temperatura)
    #---Pregunta 3 BONUSSS----#
    elif(NumeroElejido == 3):
        print('Temperatura mas alta de la lista : ', max (TemperaturaCorporal))
        print('Temperatura mas bajade la lista : ', min (TemperaturaCorporal))
        print('En 24 horas la temperatura es tomada cada : ', len (TemperaturaCorporal)/ 24, 'horas')
    #----Salida del codigo----#
    else: 
        print('opcion invalida, elija una opcion valida')
    NumeroElejido = int(input(PreguntaNumero))

print('Gracias por la informacion lo esperamos pronto' )
