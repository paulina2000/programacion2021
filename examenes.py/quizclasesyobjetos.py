class Digitales ():
    def __init__ (self, nombreIn, creadorIn, fechaPublicacionIn, generoIn, duraciónIn):
        print ('Estas son algunas características de esta app de musica')
        self.nombre = nombreIn
        self.creador = creadorIn
        self.fechaPublicacion = fechaPublicacionIn


    def todosAtributos (self):
        print (f''' Hola el nombre de esta plataforma es {self.nombre} es una plataforma nueva
                creada por {self.creador} en la fecha {self.fechaPublicacion}
    ''')

digitales1 = Digitales('spott','laura', 'julio23')
digitales.todosAtributos()

#--- punto 2 ---#

class cancion (Digitales):
    def __init__ (self, nombreIn, creadorIn, fechaPublicacionIn, generoIn, duraciónIn)
    Digitales.__init__(self,nombreIn, creadorIn, fechaPublicacionIn ):
        self.genero = generoIn
        self.duracion = duraciónIn
        print (f'la nueva cancion se llama {self.nombre} y salio el {self.fechaPublicacion}')
    def reproducir (self, veces):
        for i in range (veces):
            print (f'{self.nombre} reproduciendose {i+1} veces')

#---ultimo punto---#



