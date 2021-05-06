#----persona---#
print(60*'1')

class Personita ():
    def __init__ (self, nameIn, ageIn, idIn):
        self.name = nameIn
        self.age = ageIn
        self.id = idIn
    def hablar (self, mensaje):
        print(f'''Hola mi nombre es {self.name} 
        y tengo {self.age} mi identificacion es {self.id} y 
        ''', mensaje)
    def cantidadPasos (self, Pasos):
        for i in range (Pasos):
            print (f' {self.name} ha dado {i+1} pasos')

personita1 = Personita('german', 34, 6675578)
personita1.hablar ('me encanta salir a caminar con toda mi familia todos los dias')
personita1.cantidadPasos (300)

print(60*'2')
#----Doctor---#

class Doctor (Personita):