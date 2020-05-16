from POO.Animal import Animal
from POO.Persona import Persona


class Principal():
    jorge = Persona("Jorge Morales", 21)
    jorge.saludar()

    ana = Persona("Ana Morales", 18)
    ana.saludar()

    bobi = Animal("Bobi")
    bobi.caminar()

    jorge.adoptarMascota(bobi)#relación entre objetos

    jorge.obtenerListaDeMascotas()

    ana.adoptarMascota(bobi) # relación entre objetos
    ana.obtenerListaDeMascotas()


