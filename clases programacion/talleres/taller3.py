#----Constantes punto 1----#
NUMERO_A = 26
NUMERO_B = 70

#----Entrada al codigo----#
print("#"*15,"numero A es mayor o igual que numero B", "#"*15)
IsMayorAqueB = NUMERO_A >= NUMERO_B
print(IsMayorAqueB)

#----Constante punto 2----#
PREGUNTA_EDAD = "Cuantos años tienes? : "
MENSAJE_MENOR_EDAD = "Eres menor de edad aún creo que no puedes entrar a la disco"
MENSAJE_JOVEN = "Eres mayor de edad puedes entrar amigo"
MENSAJE_ADULTO = "Eres adulto ya puedes entrar a esta discoteca"
MENSAJE_VIEJITO = "Amigo le ayudo a buscar alguna direccion esta muy mayor para esta discoteca"


#----Entrada al codigo----#
años = int(input(PREGUNTA_EDAD)
isSinCedula = años < 18
isJoven = años >= 19 and años <= 25
isAdulto = años >= 26 and años <= 60
isAdultoMayor = años > 60 
resultado = ""
if(isSinCedula):
    print(MENSAJE_MENOR_EDAD)
elif(isJoven):
    print (MENSAJE_JOVEN)
elif(isAdulto):
    print (MENSAJE_ADULTO)
else:
    print (MENSAJE_VIEJITO)

print (resultado)



