def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
'''SE NAO TIVER O "GUILHERME" APOS O NOME DARA ERRO POIS A FUNÇÃO TEM O NOME,
POREM SE FOR COLOCADO POR EXEMPLO OUTRO VALOR, SERÁ EXECUTADO NORMALMENTE exibir_mensagem_2("GUI")'''
exibir_mensagem_3()  # SE NAO FOR DADO NENHUM VALOR, ELE PUXARA O VALOR DA FUNÇÃO
exibir_mensagem_3(nome="Chappie")  # SERA RETORNADO CHAPPIE AO INVEZ DE ANONIMO
