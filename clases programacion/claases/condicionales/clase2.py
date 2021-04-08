# estos son booleans que son solo variables
# verdadero o falso
pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
# estos son datos generales sobre mi
edad = 20
estatura = 1.75
peso = 61
NOMBRE = "Paulina Orozco Ruiz"
# aqui preguntamos si soy mayor de edad
print ("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
# aqui preguntamos si soy mas baja de la estatura promedio
print ("#"*15,"bajo la estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# aquí preguntamos si mi peso es diferente a 84
print ("#"*15,"peso diferente 84", "#"*15)
isPesoDiferente = peso != 84
print (isPesoDiferente) 
# vamos a ver si un apellido esta en el nombre completo
apellido = "mejia"
isApellido = apellido in NOMBRE
print ("#"*15,"esta apellido en el nombre", "#"*15)
print (isApellido)
