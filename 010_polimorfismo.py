class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(self.nombre,' camina')

class Ciclista(Persona):

    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print(self.nombre,' pedalea')

def main():
    persona = Persona('Juan')
    persona.avanza()

    ciclista = Ciclista('Jaime')
    ciclista.avanza()

if __name__ == '__main__':
    main()