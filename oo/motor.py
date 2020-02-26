"""
O Motor terá a responsabilidade de controlar a velociadde.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrmentar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

    Exemplo:
    # Testando o Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # Criar um objeto do tipo carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    >>> 1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    >>> 2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    >>> 0

"""


class Motor:
    # dander init (__init__)
    def __init__(self, ):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

    def calcular_velocidade(self):
        return self.velocidade


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
