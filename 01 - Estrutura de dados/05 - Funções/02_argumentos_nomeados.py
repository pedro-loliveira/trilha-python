def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
'''
Erro muito comum, como nao está nomeado, caso a função seja alterada a ordem, logo
ficando (modelo, marca, placa, ano), o que faria o banco de dados ficar uma zona.
'''
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
'''
Porem tbm tem o problema do nome do argumento ser alterado (modeloY), assim não
seria encontrada (modelo=) na função, oq ocorreria um erro.
'''
salvar_carro(**{"marca": "Fiat", "modelo": "Palio",
             "ano": 1999, "placa": "ABC-1234"})
'''
Parecido com o caso anterior, porem ** transforma em um dicionario.
'''
