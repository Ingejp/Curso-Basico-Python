class Persona():
    #atributos de clase
    __nombrePersona=''
    __edad=''
    __mascotas={}

    def __init__(self, nombre, edad):
        self.__nombrePersona=nombre
        self.__edad=edad

    def saludar(self):
        print("Hola desde la clase, mi nombre es " + str(self.obtenerNombre()) + " y tengo  " + str(self.obtenerEdad()) + " años de edad" )

    # getName(self):
    def obtenerNombre(self):
        return self.__nombrePersona

    def obtenerEdad(self):
        return  self.__edad

    def adoptarMascota(self, Animal):
        self.__mascotas={"mascota1": str(Animal.obtenerNombre())}

    def obtenerListaDeMascotas(self):
        print(self.__mascotas["mascota1"])

