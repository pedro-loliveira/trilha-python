'''
Crie uma classe Lampada que gerencia o estado de uma lâmpada:
Atributos: ligada (bool, inicia como False).
Métodos:
ligar(): marca a lâmpada como ligada.
desligar(): marca a lâmpada como desligada.
verificar_estado(): retorna "Ligada" ou "Desligada".
'''


class Lampada:
    def __init__(self):
        self.ligada = False  # incorreto: self.lampada = False

    def ligar(self):  # tinha colocado lampada
        self.ligada = True
        print("Lampada Ligada")
        # errado
        # self.lampada = lampada
        # if lampada == False:
        #     return lampada == True
        # else:
        #     return False
        # Altere o estado para ligada

    def desligar(self):  # tinha colocado lampada
        self.ligada = False
        print("Lampada desligada")
        # errado
        # self.lampada = lampada
        # if lampada == True:
        #     return lampada == False
        # else:
        #     return False
        # # Altere o estado para desligada

    def verificar_estado(self):
        if self.ligada:
            return "Ligada"
        else:
            return "Desligada"
        # Retorne o estado formatado


# Teste da classe
if __name__ == "__main__":
    lampada = Lampada()

    # Entrada do comando
    comando = input("Digite 'ligar' ou 'desligar': ").strip().lower()

    # Execute o comando
    if comando == "ligar":
        lampada.ligar()
    elif comando == "desligar":
        lampada.desligar()
    else:
        print("Comando inválido!")

    # Exiba o estado atual da lâmpada
    print(f"Estado da lâmpada: {lampada.verificar_estado()}")
