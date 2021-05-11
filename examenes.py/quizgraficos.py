import matplotlib.pyplot as plt

#---punto 1---#


PREGUNTA_SNAK = 'Cuales es tu top 5 de snaks favorito?  : '
PREGUNTA_PRECIOS = 'Cuales son los precios de esos productos que elejiste? : '
snaks= []
n=5
while(n>0):
    snak = input (PREGUNTA_SNAK)
    snaks.append(snak)
    n= n-1

precios=[]
n=5
while(n>0):
    precio = int (input(PREGUNTA_PRECIOS))
    precios.append(precio)
    n=n-1


#----Grafico de barras----#

plt.bar(snaks, precios, width= 0.7, color= 'b' )
plt.title('top 5 snaks favoritos con sus precios')
plt.xlabel('top 5 snaks')
plt.ylabel('precios de los snaks')
plt.savefig ('graficoSnaks.png')

plt.show()


#---punto 2---#

PREGUNTA_CIUDADES= 'Cuales son tus 5 ciudades favoritas? : '
PREGUNTA_POBLACION = 'Cual es la poblacion respectiva? : '
ciudades= []
n=5

while(n>0):
    ciudad = input (PREGUNTA_CIUDADES)
    ciudades.append (ciudad)
    n= n-1

poblaciones= []
n= 5

while(n>0):
    poblacion = int (input(PREGUNTA_POBLACION))
    poblaciones.append (poblacion)
    n=n-1

pieExplode = [0,0,0,1,0]
plt.pie(poblaciones, labels=ciudades)
plt.title('ciudades favoritas y su poblacion')
plt.savefig('tortaCiudades.png')

plt.show()

#----punto 3----#

import pandas as pd
import matplotlib.pyplot as plt
ppgData = pd.read_csv('ppg.csv', encoding='UTF-8',header=0, delimiter=';').to_dict()

muestras = list(ppgData['muestra'].values())
valores = list(ppgData['valor'].values())
plt.plot (muestras, valores)
plt.xlabel('tiempo (ms)')
plt.ylabel('voltaje(mV)')
plt.title('fotopletisnografia')
plt.savefig('ppg.png')

plt.show()


ecgData = pd.read_csv('ecg.csv', encoding='UTF-8',header=0, delimiter=';').to_dict()

muestras = list(ecgData['muestra'].values())
valores = list(ecgData['valor'].values())
plt.plot (muestras, valores)
plt.xlabel('tiempo (ms)')
plt.ylabel('voltaje(mV)')
plt.title('electrocardiograma')
plt.savefig('ecg.png')

plt.show()