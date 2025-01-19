class Bicicleta:  # primeira coisa e adicionar o nome da classe
    def __init__(self, cor, modelo, ano, valor):  # __init__metodo construtor
        # O método init do python é uma função especial que podemos aplicar para inicializar uma classe.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

# Self representa uma instancia da classe. Com ele e possivel acessar atributos e metodos
# de uma classe, e responsabel por vincular os atributos com os argumentos enviados
# para uma funçãoou metodo. E tambem e uma convenção ser chamado de SELF.

    def buzinar(self):  # se parece muito com função, porem e um metodo, que por convenção
        # e acompanhado de (self) assim sendo um metodo
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        # __str__ tem como objetivo fornecer uma representação legível e amigável para
        # humanos de um objeto. É o que é chamado quando você imprime um objeto ou
        # usa a função embutida
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# O método interno __class__ permite que possamos fazer uma referência a classe atual, permitindo o acesso a informações da mesma
# Ao executar seu script, a variável __name__ é igual a __main__. Ao importar o script que a contém, ela terá o nome do script.
# A partir do código acima, podemos observar que quando __dict__ é chamado para o objeto da classe Bicicleta, obtemos o
# dicionário para os atributos definidos e quando a mesma função é chamada diretamente para a classe, obtemos todas as
# variáveis ​​definidas internamente.


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
