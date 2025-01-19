def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


'''
(modelo, ano, placa, / Posição apenas. Obrigatorio passar apenas o nome.
marca, motor, combustivel) Posição ou Palavra chave. Tem escolha de passar ou não apenas por nome.
'''
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat",
            motor="1.0", combustivel="Gasolina")  # valido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
            motor="1.0", combustivel="Gasolina")  # inválido
