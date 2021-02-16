# estos son booleans 
# verdadero o falso
pruebaV = True
pruebaF = False
print (pruebaV)
print (pruebaF)
# datos generales sobre mis compras 
costoBlusa = 50
costoBolso = 100
DineroQueTengo = 900
# aquí preguntamos si me alcanza para comprar
# una blusa igual para mis 3 amigas y para mi
print("#"*15,"dinero para 4 blusas", "#"*15)
print("¿con el dinero que tengo me alcanza para las 4 blusas?")
ismayorDineroQueTengo = DineroQueTengo >= 200
print(ismayorDineroQueTengo)
# aqui estamos preguntando si me puedo comprar 5 bolsos y 10 blusas
print("#"*15,"dinero para 5 bolsos y 10 blusas", "#"*15)
print ("¿puedo comprarme 5 bolsos y 10 blusas?")
ismayorDineroQueTengo = DineroQueTengo >= 1000
print (ismayorDineroQueTengo)
# aqui preguntamos si el valor del bolso es menor a el de la blusa
print("#"*15,"el valor del bolso es menor a el de la blusa", "#"*15)
isMenorCostoBolso = costoBolso < costoBlusa 
print (isMenorCostoBolso)

