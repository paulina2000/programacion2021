class Humano ():
    '''
        Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia a el nombre del usuario
        edadEntrada: Hace referencia a la edad del usuario
        estaturaEntrada: Hace referencia a la estatura del usuario


        Tiene las sisguientes acciones:


        *hablar(mensaje):
            dado un mensaje lo muestra en pantalla
        
        *mostrar atributos ()
            muestra los atributos del usuario
        '''



    def __init__(self, nombreEntrada, edadEntrada, estaturaEntrada):
        print('hola soy un humano nuevo')
        self.edad = edadEntrada
        self.raza = 'Humano'
        self.nombre = nombreEntrada
        self.estatura = estaturaEntrada
        self.dinero = 0
    
    def hablar (self, mensaje):
        print(f'hola soy {self.nombre} tengo un mensaje que decir...', mensaje)
    def mostrarAtributos (self):
        print (f'''mi nombre es {self.nombre}
                    mi estatura es {self.estatura}
                    mi edad es {self.edad}
                    lo que tengo ahorrado es {self.dinero} pesos
        ''')
    def recorrerDistancia(self, distanciaMetros):
        for i in range (distanciaMetros):
            print(f'hola soy {self.nombre} y he recorrido {i+1} metros ')

    def ahorraDinero(self):
        preguntaIngresarMontos = 'ingrese S---> para continuar añadiendo montos y N---> para finalizar : '
        preguntaMonto = ' Cuanto vas a ingresar? : '
        IngresarMontos = input(preguntaIngresarMontos)
        while(IngresarMontos != 'N' ):
            monto= float (input(preguntaMonto))
            self.dinero = self.dinero + monto
            IngresarMontos = input(preguntaIngresarMontos)
            print(f'soy {self.nombre} y tengo {self.dinero} pesos ')
        return self.dinero






humano1 = Humano('Daniel',27, 1.70)
humano2 = Humano('Mafer',27, 1.65)

humano1.hablar('espero que esten muy bien')
humano2.hablar('chao')
print(humano1.nombre)
print(humano2.nombre)
print(humano1.edad)
print(humano2.edad)
humano1.recorrerDistancia(25)
humano1.mostrarAtributos()
totalAhorrado = humano2.ahorraDinero()
humano2.mostrarAtributos()
