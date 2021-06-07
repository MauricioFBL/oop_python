##       ABSTRACCION
# Enfocarse a la informacion relevante
# Separar la idea central de los detalles secundarios
# Utilizando variables y metodos privados
class Lavadora:

    def __init__(self):
        pass
    
    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self, temperatura):
        print(f'llenando el tanqe con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo Jabon')

    def _lavar(self):
        print('lavando la ropa')

    def _centrifugar(self):
        print('centrifugando la ropa')

if __name__ == '__main__':
    Lavadora = Lavadora()
    Lavadora.lavar()
