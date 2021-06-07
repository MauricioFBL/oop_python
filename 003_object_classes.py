##       TIPOS DE DATOS ABSTRACTOS
# # Definir clases
# class <nombre_de_la_clase>(<super_clase>):
#     # funcion init o Constructor: su función es definir el estado inicial de una clase
#     def __init__(self, <parametros>): # self es el primer parametro que reciben funciones, se usa por convencion e indica que pertenece a esta clase
#         <expresion1>
#         <expresion2>
#         ...
#     # Metodos, los metodos son funciones que pertenecen a una clase
#     def <b¿nombre_del_metodo>(self, <parametros>):
#         <expresion1>
#         <expresion2>
#         ...
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} y tengo {self.edad} años.'

# uso
david = Persona('David', 35)
erika = Persona('Erika', 32)
print(david.saluda(erika))
print(erika.saluda(david))

class coordenas:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        distancia = (x_diff + y_diff)**(1/2)
        return distancia

if __name__ == '__main__':
    c1 = coordenas(12,7)
    c2 = coordenas(13,21)
    print(c1.distancia(c2))
    print(c1.distancia(c1))
    print(isinstance(c1,coordenas))