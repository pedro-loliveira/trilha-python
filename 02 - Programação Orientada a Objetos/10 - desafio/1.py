'''
Crie uma classe GerenciadorSenha que valida e armazena senhas:
Atributos: senha (string, inicia como None).
Métodos:
definir_senha(senha): define a senha se ela tiver pelo menos 6 caracteres.
validar_senha(senha): retorna True se a senha for igual à definida, False caso contrário.
status(): retorna "Senha definida" ou "Senha não definida".
'''


class GerenciadorSenha:
    def __init__(self):
        self.senha = None
        # Inicialize os atributos

    def definir_senha(self, senha):
        if len(senha) >= 6:  # if len(senha) >= 6: correçõa
            self.senha = senha  # correção
            print("Digite uma senha")  # "Senha definida com sucesso"
        else:
            print("Senha muito curta")  # ,digite pelo menos 6 numeros
        # Defina a senha se válida

    def validar_senha(self, senha):
        if self.senha == senha:
            return True
        else:
            return False
        # Valide a senha fornecida

    def status(self):
        if self.senha is not None:
            return "Senha definida"  # correçao
        else:  # correçao
            return "Senha nao definida"  # correçao


# Teste da classe
if __name__ == "__main__":  # correçao
    gerenciador = GerenciadorSenha()  # correçao

    # Definir uma senha
    senha1 = input("Digite uma senha: ")  # correçao
    gerenciador.definir_senha(senha1)  # correçao

    # Validar a senha
    senha2 = input("Digite a senha para validação: ")  # correçao
    if gerenciador.validar_senha(senha2):  # correçao
        print("Senha válida!")  # correçao
    else:  # correçao
        print("Senha inválida!")  # correçao

    # Exibir o status
    print(gerenciador.status())  # correçao

# Entrada
senha1 = input()
senha2 = input()
# Crie a instância, teste os métodos e exiba o status
