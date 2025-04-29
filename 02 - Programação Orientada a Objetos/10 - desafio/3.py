'''
Crie uma classe CalculadoraMedia que calcula a média de notas de um aluno:
Atributos: notas (lista, inicia vazia).
Métodos:
adicionar_nota(nota): adiciona uma nota à lista.
calcular_media(): retorna "Média: X.XX".
'''


class CalculadoraMedia:
    def __init__(self):
        self.lista = []
        # Inicialize os atributos

    def adicionar_nota(self, nota):
        self.lista.append(nota)
        print(f'Nota {nota}  adicionada')
        # Adicione a nota à lista

    def calcular_media(self):
        if len(self.lista) == 0:
            return "nenhuma nota adciionada"
        media = sum(self.lista) / len(self.lista)
        return f"Media: {media:.2f}"
        # Calcule e retorne a média formatada


if __name__ == '__main__':
    calculadora = CalculadoraMedia()
    # Entrada
    nota1 = float(input())
    nota2 = float(input())

    calculadora.adicionar_nota(nota1)
    calculadora.adicionar_nota(nota2)

    print(calculadora.calcular_media())
# Crie a instância, adicione notas e calcule a média
