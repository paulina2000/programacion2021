#----Constantes----#
PREGUNTA_PESO = "cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "cuanto mides en metros? : "
MENSAJE_BIENVENIDA = "hola como estas? voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "tu imc es de...."
MENSAJE_BAJO_PESO = "Estas pero delgado!! "
MENSAJE_NORMAL = "Estas en forma "
MENSAJE_SOBRE_PESO =  "Ten cuidado estas en sobrepeso" 
MENSAJE_OBESO = "cuidado estas obeso tu salud corre riesgo "

#----Entrada codigo----#
print(MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isBajoPeso = imc >= 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrePeso = imc > 25 and imc < 30
resultado = ""
if (isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_NORMAL
else :
    resultado = MENSAJE_OBESO

print (MENSAJE_DESPEDIDA, imc)
print (resultado)
