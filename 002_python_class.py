##       CLASES EN PYTHON
# Clase: molde o representacion de algo real, que dependiendo del molde que utilices tiene atributos diferentes
# Definir clases

class <nombre_de_la_clase>(<super_clase>):
    # funcion init o Constructor: a mi parecer, es uno de los elemntos más importantes en POO, ya que permite el polimorfismo y,
    # su función es definir el estado inicial de los atributos de una clase
    def __init__(self, <parametros>): # self es un termino usado por convencion, es el primer parametro que reciben las funciones, e indica que una funcion pertenece a esta clase
        <expresion1>
        <expresion2>
        ...

    # Metodos, los metodos son funciones que pertenecen a una clase
    def <nombre_del_metodo>(self, <parametros>):
        <expresion1>
        <expresion2>
        ...

# Instancias: forma de accesoa una clase y a sus metodos
# Instanciar clase
variable = <nombre_de_la_clase>(<parametros>)
# Usar metodos de una clase
variable.<nombre_del_metodo>(parametros)