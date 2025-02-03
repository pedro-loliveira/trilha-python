# Crie uma classe Produto que representa um item em um estoque:
# Atributos: nome (string), quantidade (int).
# Métodos:
# adicionar_estoque(qtd): aumenta a quantidade em estoque.
# remover_estoque(qtd): diminui a quantidade, mas não permite valores negativos.
# exibir_estoque(): retorna "Produto: X, Quantidade: Y".


class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        # Inicialize os atributos

    def adicionar_estoque(self, qtd):
        self.quantidade += qtd
        # Adicione ao estoque

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd

    def exibir_estoque(self):
        return f"Produto: {self.nome} / Quantidade: {self.quantidade}"


# Entrada
nome_produto = input()
quantidade_inicial = int(input())
qtd_adicionar = int(input())
qtd_remover = int(input())

produto = Produto(nome_produto, quantidade_inicial)

produto.adicionar_estoque(qtd_adicionar)
produto.remover_estoque(qtd_remover)

print(produto.exibir_estoque())
