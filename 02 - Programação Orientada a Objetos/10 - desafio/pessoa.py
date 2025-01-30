class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


'''
Os atributos nome e idade já foram definidos no __init__. O método apenas 
acessa esses valores, não precisa redefini-los.
Isso geraria um erro, pois:
O parâmetro nome não foi passado para o método.
Atributos devem ser inicializados no __init__, não em métodos secundários.
def exibir_informacoes(self):
    self.nome = nome  > Errado! "nome" não existe neste escopo
'''

nome = input()
idade = int(input())

pessoa = Pessoa(nome, idade)  # Transformamos os dados de entrada (input) em um
# objeto concreto com estado próprio. A instância pessoa carrega consigo os
# valores específicos fornecidos pelo usuário.
print(pessoa.exibir_informacoes())
'''
Encapsulamento em ação: O objeto pessoa (com p minusculo nao e a classe)sabe 
como exibir seus próprios dados graças ao método que implementamos.
A mensagem é gerada internamente pelo objeto, seguindo o princípio de que cada
classe é responsável por seu próprio comportamento.
'''

# Sobre desafios "calculadora" e "dados_pessoais"
'''
#Similaridades:
Encapsulamento: Ambos os objetos gerenciam seus próprios dados e comportamentos.
Métodos com responsabilidades claras: soma() faz cálculos, exibir_informacoes() 
formata saída.
#Diferenças:
Estado do objeto:
A Calculadora não armazena dados (não tem atributos).
A Pessoa possui estado (nome e idade são armazenados como atributos).
'''


'''
Conceitos-Chave de POO Aplicados:
Encapsulamento: A classe Pessoa encapsula dados (nome, idade) e o comportamento 
(como exibi-los).
Mensagens entre objetos: Pedimos ao objeto que execute uma ação 
(exibir_informacoes()) em vez de manipular seus dados diretamente.
Estado vs Comportamento: Atributos armazenam estado, métodos definem 
comportamento.
'''
