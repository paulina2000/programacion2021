#----Grafico de barras ingresos 2020 mes a mes de una persona'
import matplotlib.pyplot as plt 
mes = ['ene','feb','mar','abr','may','jun','jul','agost','sept','oct', 'nov','dici']
dineroGanado = [850.000, 900.000, 780.000, 820.500, 990.000, 630.000, 880.500, 700.000, 860.900, 500.800, 890.000, 990.000]
plt.bar(mes, dineroGanado, width=0.6, color= 'r')
#---titulos---#
plt.title('salarios colombianos mes a mes año 2020')
plt.xlabel('mes del año 2020')
plt.ylabel('ingresos mensuales')
####################
plt.show()


#----Grafico de torta ciudades colombia con su area ----#
import matplotlib.pyplot as plt 
#-- labels= nobres ciudades colombia--#
pieLabels =['Cartagena', 'Bogota', 'Cali', 'Manizales', 'Bucaramanga']
#---sizes= tamaño de cada ciudad en Area km y porcentaje de cada una por 2000 habitantes ---#
#---sizes= 572, 1587, 564, 571, 162
sizes = [15, 55, 11, 14, 5 ]
pieExplode = [0,0,0,0,0]

plt.pie(sizes,labels=pieLabels)
##########################################
plt.title('ciudades de colombia porcentaje por 2.000 habitantes')
##########################################
plt.show()



#---Fotoplestimograma---#

import pandas as pd 
ppgData = pd.read_csv('ppg.csv', encoding='UTF-8',header=0, delimiter=';').to_dict()

muestras = list(ppgData['muestra'].values())
valores = list(ppgData['valor'].values())
plt.plot (muestras, valores)
plt.xlabel('tiempo(ms)')
plt.ylabel('voltaje(mV)')
plt.title('Fotoplestimograma')
plt.show()