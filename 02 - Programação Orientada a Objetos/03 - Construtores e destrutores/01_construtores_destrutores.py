class Cachorro:
    def __init__(self, nome, cor, acordado=True):  # Metodo construtor, esmpre
        # executado quando uma nova instancia da classe e criada
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):  # Metodo destrutor
        # Ele é chamado depois que ocorre a coleta de lixo de um objeto, o que
        # acontece depois que todas as referências ao item foram destruídas.
        # Mas raramente e utilizado, pois o python ja tem esse costume.
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
