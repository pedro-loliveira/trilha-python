def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna()
    funcao_2()  # so da pra chamar a função secundaria dentro da primaria, assim
    # quando a primaria for chamada, chama a secundaria, mas se a secundaria for
    # chamada fora da primaria, dara erro

# funcao_interna() #erro
# funcao_2() #erro


principal()
