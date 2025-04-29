'''
Crie uma classe Retangulo que calcula área e perímetro:
Atributos: largura e altura (float).
Métodos:
calcular_area(): retorna largura * altura.
calcular_perimetro(): retorna 2*(largura + altura).
'''


class Retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura
        # TODO: Inicialize os atributos

    def calcular_area(self):
        return self.largura * self.altura  # ja q tem o INIT nao precisa definir so puxar

    def calcular_perimetro(self):
        # ja q tem o INIT nao precisa definir so puxar
        return 2*(self.largura + self.altura)

        # Entrada
largura = float(input())
altura = float(input())  # até essa parte eu msm fiz
#  Crie a instância e exiba área e perímetro
# nicializa o objeto com as dimensões fornecidas.
retangulo = Retangulo(largura, altura)
# Calcula e imprime os resultados
print(retangulo.calcular_area())
print(retangulo.calcular_perimetro())
