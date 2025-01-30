'''
Crie uma classe Produto que representa um item em um estoque:
Atributos: nome (string), quantidade (int).
Métodos:
adicionar_estoque(qtd): aumenta a quantidade em estoque.
remover_estoque(qtd): diminui a quantidade, mas não permite valores negativos.
exibir_estoque(): retorna "Produto: X, Quantidade: Y".
'''


class Produto:
    def __init__(self, nome, quantidade):
        # TODO: Inicialize os atributos

    def adicionar_estoque(self, qtd):
        # TODO: Adicione ao estoque

    def remover_estoque(self, qtd):
        # TODO: Remova do estoque com validação

    def exibir_estoque(self):
        # TODO: Retorne as informações formatadas

        # Entrada
nome_produto = input()
quantidade_inicial = int(input())
qtd_adicionar = int(input())
qtd_remover = int(input())

# TODO: Crie a instância e teste os métodos
