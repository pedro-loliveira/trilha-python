'''
O desafio consiste em implementar uma classe Calculadora que utilize os 
princípios da Programação Orientada a Objetos (POO). A classe deve conter 
um método para realizar a operação de soma entre dois números inteiros, 
encapsulando assim a lógica matemática da adição.
'''
# Forma correta do jeito que o desafio pede:


class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2


num1 = int(input())
num2 = int(input())
calc = Calculadora()
resultado = calc.soma(num1, num2)
print(resultado)

# Porem tentei fazer com self.num1=num1
'''
Só faria sentido se os números precisassem ser armazenados para uso 
posterior em outros métodos. Por exemplo:
'''


class CalculadoraComMemoria:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def define_numeros(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2


'''
Neste caso, os números são armazenados no objeto porque há uma necessidade 
explícita de manter estado entre chamadas de métodos.
'''
