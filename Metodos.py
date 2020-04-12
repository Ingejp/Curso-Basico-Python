#sin parametros
"""
def saludar():
    print("Saludos desde el primer metodo con Python")

saludar()"""
"""
def sumar():
    primerNumero=10
    segundoNumero=20
    resultado=primerNumero+segundoNumero
    return resultado

print(sumar())

def sumar(primerNumero, segundoNumero):
    resultado=primerNumero+segundoNumero
    return resultado

#print(sumar(5,20))

print(sumar(100,200))"""

"""def sumaNParametros(primerParametro, *tuplaNumeros):
    for valor in tuplaNumeros:
        resultado=primerParametro + valor
        print(resultado)

#sumaNParametros(5, 10,15)

sumaNParametros(5, 20, 25, 30, 40)"""


def sumarNParametros(primerParametro, **diccionario):
    for nota in diccionario.items():
        print(nota)

sumarNParametros(5, primerCurso=9, segundoCurso=8, tercerCurso=10)