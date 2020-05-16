class Animal():
    #atributos de clase
    tipoDeAnimal=''
    __nombre=''

    def __init__(self, nombre):
        self.tipoDeAnimal='PERRO'
        self.__nombre= nombre

    def caminar(self):
        print("estoy caminando")

    def obtenerNombre(self):
        return self.__nombre

