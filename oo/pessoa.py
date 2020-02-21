class Pessoa:
    # Atributo default ou de Classe
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá! {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 7

    @classmethod
    def nome_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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

    francisco.olhos = 1
    del francisco.olhos

    # __dict__ mostra os atributos de instância
    print(francisco.__dict__)
    print(guilherme.__dict__)
    print(gabriel.__dict__)

    Pessoa.olhos = 3

    print(Pessoa.olhos)
    print(francisco.olhos)
    print(guilherme.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(francisco.olhos), id(guilherme.olhos), id(gabriel.olhos))

    print(Pessoa.metodo_estatico(), francisco.metodo_estatico())

    print(Pessoa.nome_atributos_de_classe(), francisco.nome_atributos_de_classe())