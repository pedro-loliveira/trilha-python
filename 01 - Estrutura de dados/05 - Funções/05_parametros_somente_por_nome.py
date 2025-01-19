def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


'''
Tudo que estiver antes da barra (/) e obrigatorio ser apenas nome. Tudo que for após asteristico
(*) e obrigatorio ser apenas nomeado.
'''
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat",
            motor="1.0", combustivel="Gasolina")  # valido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
            motor="1.0", combustivel="Gasolina")  # inválido

# 1 opcional


def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


'''
Exemplo onde um dos argumentos e opcional. Mo caso "MARCA"
'''

# Todos nomeados obrigatoriamente


def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
