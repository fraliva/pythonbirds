class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá! {id(self)}'

if __name__=='__main__':
    guilherme = Pessoa(nome='Guilherme')
    gabriel = Pessoa(nome='Gabriel')
    francisco = Pessoa(guilherme, gabriel, nome='Francisco')

    print(Pessoa.cumprimentar(francisco))
    print(id(francisco))
    print(francisco.cumprimentar())
    print(francisco.nome)
    print(francisco.idade)

    for filho in francisco.filhos:
        print(filho.nome)

    # Atributo criado dinamicamente - não é uma boa prática
    francisco.sobrenome = 'Valente'
    print(francisco.sobrenome)

    # É possível remover os atributos dinamicamente também
    del francisco.filhos

    print(francisco.__dict__)
    print(guilherme.__dict__)
    print(gabriel.__dict__)

