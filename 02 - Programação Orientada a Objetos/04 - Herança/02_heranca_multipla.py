class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


'''
O IDE junto do python se perdem, pois em um tem 2 argumentos, e no outro tbm. Porem so e passado
3 argumentos, quando deveriam ser 4. Com isso se usa Kwargs, assim todo argumento novo na classe base
vai ser passado super().__init__(**kw). Resumindo, tudo apos o **Kw vai ser opcional. Mas tem de ser
passado de forma nomeada nro_patas=nro_patas.
'''


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


'''
A super()função é usada para dar acesso a métodos e propriedades de uma classe pai ou irmã.
A super()função retorna um objeto que representa a classe pai.
'''
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(
    nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)

'''
__mro__ busca a forma que o interpretador vai fazer a resolução, a ordem etc. Muito bom para
esse tipo de problemas. "Classe".mro() tbm funciona
'''
