#----Constantes----#
PREGUNTA_NIVEL_TRIGLICERIDOS = "En que nivel estan los trigliceridos del paciente? : "
PREGUNTA_NIVEL_HOMOCISTEINA = "En que nivel esta la homocisteina del paciente? : "
MENSAJE_OPTIMOS_TRI = "El nivel de trigliceridos del paciente estan muy bien"
MENSAJE_OPTIMOS_HOMO= "lods niveles de homocisteina del paciente estan muy bien"
MENSAJE_SOBRE_LIMITE_TRI = "El nivel de trigliceridos está algo sobre el limite"
MENSAJE_SOBRE_LIMITE_HOMO = "los niveles de homocisteina están algo sobre el limite"
MENSAJE_ALTO_TRI = "El nivel de trigliceridos esta alto"
MENSAJE_ALTO_HOMO = "Los niveles de homocisteina estan altos"
MENSAJE_MUYALTO_TRI = "El nivel de trigliceridos esta demasiado alto"
MENSAJE_MUYALTO_HOMO = "Los niveles de homocisteina estan demasiado altos"

#----Entrada al codigo----#
trigliceridos = int(input(PREGUNTA_NIVEL_TRIGLICERIDOS))
homocisteina = int(input(PREGUNTA_NIVEL_HOMOCISTEINA))
isOptimoTri = trigliceridos < 150 
isOptimoHomo = homocisteina >= 2 and homocisteina <= 15
isSobreLimiteTri = trigliceridos >= 150 and trigliceridos <= 199
isSobreLimiteHomo = homocisteina > 15 and homocisteina <= 30
isAltoTri = trigliceridos >= 200 and trigliceridos <= 499
isAltoHomo = homocisteina > 30 and homocisteina < 100
isMuyAltoTri = trigliceridos > 500
isMuyAltoHomo = homocisteina > 100

if(isOptimoTri):
    resultado = MENSAJE_OPTIMOS_TRI
elif(isSobreLimiteTri):
    resultado = MENSAJE_SOBRE_LIMITE_TRI
elif(isAltoTri):
    resultado = MENSAJE_ALTO_TRI
else:
    resultado = MENSAJE_MUYALTO_TRI


print(resultado)

if(isOptimoHomo):
    resultadoH = MENSAJE_OPTIMOS_HOMO
elif(isSobreLimiteHomo):
    resultadoH = MENSAJE_SOBRE_LIMITE_HOMO
elif(isAltoHomo):
    resultadoH = MENSAJE_ALTO_HOMO
else:
    resultadoH = MENSAJE_MUYALTO_HOMO

print(resultadoH)


