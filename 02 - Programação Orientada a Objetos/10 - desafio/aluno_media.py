'''
Crie uma classe Aluno que armazene notas e calcule a média:
Atributos: nome (string), notas (lista de floats).
Métodos:
adicionar_nota(nota): adiciona uma nota à lista.
calcular_media(): retorna a média das notas.
'''

# class Aluno:
#     def __init__(self, nome):
#         #  Inicialize os atributos

#     def adicionar_nota(self, nota):

#         #  Adicione a nota à lista

#     def calcular_media(self):
#         #  Calcule a média

#         # Entrada
# nome_aluno = input()
# nota1 = float(input())
# nota2 = float(input())

#  Crie a instância, adicione notas e exiba a média


class Aluno:
    def __init__(self, nome):
        self.nome = nome  # Atributo para armazenar o nome do aluno
        self.notas = []   # Lista vazia para armazenar as notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)  # Adiciona uma nova nota à lista

    def calcular_media(self):
        # Calcula a média somando todas as notas e dividindo pela quantidade
        return sum(self.notas) / len(self.notas)


# Entrada do usuário
nome_aluno = input()
nota1 = float(input())
nota2 = float(input())

# Cria uma instância do Aluno
aluno = Aluno(nome_aluno)

# Adiciona as notas ao objeto aluno
aluno.adicionar_nota(nota1)
aluno.adicionar_nota(nota2)

# Calcula e imprime a média
media = aluno.calcular_media()
print(media)
