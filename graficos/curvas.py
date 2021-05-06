import matplotlib.pyplot as plt 

tiempo =[0,1,2,3,4,5]
sensor =[4,5,6,8,9,10]
plt.plot(tiempo,sensor, '---, r')
#################################
plt.title ('grafico sensor contra el tiempo')
plt.xlabel ('tiempo(s)')
plt.savefig ('sensor')
#################################

plt.show()

diccionario ={}
diccionario ['nombresEstudiantes'] = ['jacobo', 'dani', 'Maria', 'Elena']
diccionario['EdadesEstudiantes'] = [18, 17,24, 32]
diccionario ['peso'] = [84,56,64,57]
print (diccionario)

print (diccionario['nombresEstudiantes'][-1], diccionario['EdadesEstudiantes'][-1])


