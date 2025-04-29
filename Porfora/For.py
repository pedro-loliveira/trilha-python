"""
O laço for em Python serve para iterar sobre elementos de uma sequência
(como listas, tuplas, strings) ou qualquer objeto iterável (como dicionários,
arquivos, geradores, etc.). A cada iteração, o for “pega” um elemento do iterável
e executa um bloco de código com ele.

for variável in iterável:
bloco de código que usa 'variável'

variável: nome que você dá ao item atual da iteração. A cada volta do laço, ela recebe o próximo elemento de iterável.
iterável: objeto que produz uma sequência de valores (lista, tupla, string, range, dicionário, etc.).

*Percorrendo uma lista
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(f'Eu gosto de {fruta}')
*Saida
Eu gosto de maçã
Eu gosto de banana
Eu gosto de laranja

Nota> Então ele vai printar "Eu gosto de" quantas vezes tiver na lista.

*Usando range()
-range(n) gera números de 0 a n-1.
-range(a, b) gera de a até b-1.
-range(a, b, passo) pula de passo em passo.

for i in range(5):
print(i)
*Saida: 0, 1, 2, 3, 4
for i in range(1, 6):
print(i)
*Saida: 1, 2, 3, 4, 5
for i in range(0, 11, 2):
print(i)
*Saida: 0, 2, 4, 6, 8, 10

Nota¹> Em Python (e em muitas outras linguagens), o nome que você dá à variável 
do laço for é totalmente arbitrário — o famoso i é só uma convenção que vem de 
“índice” (do inglês index), mas poderia ser qualquer outro nome.

Nota²>Ou seja, i não está dentro do range, mas sim recebe cada elemento que o 
range produz. Se você quisesse, poderia escrever "numero".

*Iterando sobre uma string
palavra = "Python"
for letra in palavra:
    print(letra.upper())
SAIDA:
P
Y
T
H
O
N

Nota> Como e uma string cada letra faz parte de uma lista basicamente.

*Iterando sobre um dicionário
aluno = {'nome': 'Ana', 
        'idade': 22, 
        'curso': 'Engenharia'}
for chave in aluno:
    print(chave)
SAIDA: só chaves

aluno = {'nome': 'Ana', 
        'idade': 22, 
        'curso': 'Engenharia'}
for chave, valor in aluno.items():
    print(chave, '→', valor)
SAIDA: chaves e valores

*Controle de fluxo dentro do for
-BREAK
for n in range(10):
    if n == 5:
        break     # sai do for quando n for 5
    print(n)
SAIDA: 0,1,2,3,4

-CONTINUE
for n in range(6):
    if n % 2 == 0:
        continue  # pula números pares
    print(n)
SAIDA: 1,3,5

-IF ELSE
for n in range(3):
    print(n)
else:
    print("Laço concluído sem interrupção.")

*Quando usar for em vez de while
Use FOR sempre que souber antecipadamente que deseja iterar sobre cada item de 
uma coleção ou de um intervalo de valores.
Use while quando o número de iterações depender de uma condição que muda durante 
a execução e não de uma coleção finita.
    """
# Exercício rápido
# Dada uma lista de números, crie um for que calcule a soma apenas dos números ímpares.
numeros = [1, 4, 7, 10, 13, 16]
soma_impares = 0

for n in numeros:
    # verifica se n é ímpar
    if n % 2 != 0:  # != operador de desigualdade
        soma_impares += n   # o operador += acumula o valor de n em soma_impares
print("Soma dos ímpares:", soma_impares)

'''
Uso comum do modulo %
if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é ímpar")
'''
