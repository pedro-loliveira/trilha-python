'''
Descrição:
Crie uma classe ContaBancaria que representa uma conta bancária simples. A classe deve ter:
Atributos: saldo (inicializado com 0)
M
depositar(valor): adiciona o valor ao saldo.
sacar(valor): subtrai o valor do saldo, mas só permite saque se houver saldo suficiente.
exibir_saldo(): retorna uma string formatada como "Saldo: R$X.XX".
'''


class ContaBancaria:
    def __init__(self):
        # Inicializa o saldo com 0
        self.saldo = 0

    def depositar(self, valor):
        # Adiciona o valor ao saldo
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        # Subtrai o valor do saldo, se houver saldo suficiente
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")

    def exibir_saldo(self):
        # Retorna o saldo formatado como "Saldo: R$X.XX"
        return f"Saldo: R${self.saldo:.2f}"


# Testando a classe
if __name__ == "__main__":
    # Cria uma instância da classe ContaBancaria
    conta = ContaBancaria()

    # Entrada de valores
    valor_deposito = float(input("Digite o valor para depósito: "))
    valor_saque = float(input("Digite o valor para saque: "))

    # Realiza as operações
    conta.depositar(valor_deposito)
    conta.sacar(valor_saque)

    # Exibe o saldo final
    print(conta.exibir_saldo())
