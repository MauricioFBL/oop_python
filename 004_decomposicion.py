##       DECOMPOSICION
# Fragmentar soluciones a manera de poder reutilizarlos 
class Automovil:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros = 4)

    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento'


class Motor:
    def __init__(self, cilindros, tipo = "gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass
        
