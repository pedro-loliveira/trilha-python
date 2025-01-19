def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


# Na fnção nao e necessario ter os nomes ARGS e KWARGS apenas suceder de * ou **
'''
Tudo que vir após a data_extenso, o python reconhece como *(args) e so irá parar
quando reconhecer **(karwgs) que e uma extrutura chave do valor 
'''

exibir_poema(
    "Sexta, 26 de agosto de 2022"
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

'''
ARGS
O *args é uma expressão comum em Python que permite passar um número arbitrário
de argumentos para uma função. Esses argumentos são agrupados em uma tupla antes 
de serem passados para a função. Aqui está um exemplo simples para ilustrar *args:
'''


def func(*args):
    for a in args:
        print(a)


func(1)
func(1, 2, 3)

'''
KWARGS
De maneira similar, **kwargs faz com que uma função aceite argumentos nomeados 
arbitrários, isto é, argumentos que você passa para a função com a estrutura 
nome="valor". O **kwargs coleta todos os argumentos de palavra-chave em um dicionário, 
onde a chave é o nome do parâmetro, e seu valor correspondente é o valor entregue à 
função. Veja o exemplo a seguir:
'''


def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


func(name='Juliano', age=27)
