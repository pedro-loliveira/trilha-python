# Cagada que eu fiz:
# class ConversorTemperatura:
#   def celsius_para_fahrenheit(self, fahrenheit, celsius):
#       self.fahrenheit = fahrenheit
#       self.celsius = celsius
#     return fahrenheit(celsius*95)+32fahrenheit=(celsius*59)+32
# celsius = float(input())
# conversor = celsius_para_fahrenheit()
# fahrenheit = conversor.celsius_para_fahrenheit(celsius)
# print(fahrenheit)

# Correto:
class ConversorTemperatura:
    # Serve como um "utilitário" para conversões de temperatura.
    # Não precisa armazenar estado (atributos), pois só executa cálculos pontuais.
    def celsius_para_fahrenheit(self, celsius):
        # Recebe um valor em Celsius como parâmetro.
        # Aplica a fórmula correta: (Celsius × 9/5) + 32.
        # Retorna o resultado imediatamente, sem alterar o estado do objeto.
        return (celsius * 9/5) + 32


celsius = float(input())
conversor = ConversorTemperatura()
# Criamos uma instância (conversor = ConversorTemperatura()) para acessar o método.
# O método é chamado com o valor de entrada do usuário.
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)

'''
O resultado e o proprio fahrenheit logo nao havia necessidade de coloca-lo
dentro do proprio codigo, pois ele e o resultado do calculo:
Fahrenheit=(Celsius*95)+32
Fahrenheit=(Celsius*59)+32
'''
