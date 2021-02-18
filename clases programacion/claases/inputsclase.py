# el input siempre devuelve un streem
#----Constantes----#
PREGUNTA_NOMBRE = "como te llamas? : "
PREGUNTA_EDAD = "cuantos años tienes? : "
PREGUNTA_ESTATURA = "cuanto mides? : "
MENSAJE_SALUDO = "un gusto conocerte"



#----Entrada al codigo----#
nombre = input (PREGUNTA_NOMBRE)
edad = int (input (PREGUNTA_EDAD))
print (MENSAJE_SALUDO, nombre)
print (edad+8)
estatura = float (input(PREGUNTA_ESTATURA))

