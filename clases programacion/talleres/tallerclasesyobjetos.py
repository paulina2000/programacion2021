#--- torta ---#
class Torta ():
    def __init__ (self, formaIn, saborIn, alturaIn):
        print ( 'Hola les voy a hablar sobre mis tortas')
        self.altura = alturaIn
        self.forma = formaIn
        self.sabor = saborIn

    def hablar (self):
        print (f' Esta torta es super especial ya que fue hecha con mucho amor ya veraas por que')
    def todosAtributos (self):
        print(f''' esta torta tiene una forma {self.forma} que llama mucho la atencion
                    El sabor es {self.sabor} y todos quedan matados
                    lo mejor de todo es la altura que es de {self.altura} metros
        ''')


tortaD = Torta('corazon', 'chocolate', 3)
print (tortaD.hablar)

tortaD.todosAtributos()

print (60*'2')
#---Estudiante---#
class Student ():
    def __init__ (self, nombreIn, edadIn, idIn, carreraIn, semestreIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id =idIn
        self.carrera = carreraIn
        self.semestre = semestreIn
        print(f'Hola me llamo {self.nombre} tengo {self.edad} años mi id es {self.id} estudio {self.carrera} y estoy en el semestre {self.semestre}')
    def estudiar (self, materia):
        print(f'Estoy estudiando la materia {materia} hoy')
    def tiempoEstudio (self, tiempoEstudioMateria):
        print(f'Esta materia la veo {tiempoEstudioMateria} semestres')


estudiante = Student('paulina', 19, 644657889, 'ingenieria biomedica', 'tercero')
estudiante.estudiar  ('calculo')
estudiante.tiempoEstudio (3)

print (60*'3')
#---Nutricionista---#

class Nutri ():
    def __init__ (self, nombreIn, edadIn, uniIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.universidad = uniIn
        print(f'Hola me llamo {self.nombre} tengo {self.edad} años soy su nutricionista y estudie en el {self.universidad}')
    def imc (self, pesoIn, alturaIn):
        imc = pesoIn / (alturaIn)**2
        print(f' mi indice de masa corporal es {imc} kilos')

nutri1 = Nutri( 'sara', 18, 'ces')
nutri1.imc (56, 1.70)

print (60*'4')
#---canguro---#

class Cangu ():
    def __init__ (self, nombreIn, edadIn, idIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
    def numeroSaltos (self, saltos):
        for i in range (saltos):
            print (f"Hola soy {self.nombre} y he saltado {i+1} veces")

Cangurito = Cangu('alfo', 25, 834768793885)
Cangurito.numeroSaltos (23)


#----Instrumento musical----#

class Instrumento ():
    def __init__ (self, nombreIn, tipoIn, colorIn):
        self.nombre = nombreIn
        self.tipo = tipoIn
        self.color = colorIn
    def cancion (self, nombreCancion):
        print(f'con el instrumento {self.nombre} de tipo {self.tipo} de color {self.color} vamos a tocar la cancion {nombreCancion}')

Instrumento1 = Instrumento('guitarra', 'cuerdas', 'rojo')
Instrumento1.cancion ('yo te esperare')
