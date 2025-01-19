texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:  # For consegue ler as letras das palavras, e comparar
        # com a string. Assim ele vai pegar oq o usuario enviar e checar cara letra para conferir
        # se AEIOU estão. Logo se escrever PYTHON, o resultado final e O.
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):  # 0 (start) 51 (final) 5(de quanto em quanto e contado)
    # 0 5 10 15 ...
    print(numero, end=" ")
