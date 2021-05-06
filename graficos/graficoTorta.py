#---importamos la libreria---#
import matplotlib.pyplot as plt
#---creamos los labels sizes y explode---#
#---labels: python, java, dart, js, nombres porciones de torta---#
pieLabels =[' python', 'java', 'dart', 'js']
#---sizes los tamaños de cada porcion de la torta---#
sizes = [50,25,15,10]
#---explode: que tan alejado del origen esta la torta---#
pieExplode = [0,0,2,0]
acumulador = 0
for elemento in sizes : 
    acumulador += elemento

for i in range (len(pieLabels)):
    pieLabels[i] += indicador+str(sizes[i]/acumulador*100) *'%'

plt.pie(sizes,labels=pieLabels)
###############################
plt.title('uso de lenguajes de programacion en el 2021')
plt.savefig('tortasLenguajes.png')
###############################
plt.show()

pieExplode = [0,0,0.9,0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode)
###############################
plt.title('uso de lenguajes de programacion en el 2021')
plt.savefig('tortasLenguajes.png')
###############################
plt.show()

pieExplode = [0,0,0.9,0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode,
    shadow=True, 
    startangle =45)
###############################
plt.title('uso de lenguajes de programacion en el 2021')
plt.savefig('tortasLenguajes.png')
###############################
plt.show()