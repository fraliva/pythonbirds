class Pessoa:
    # Atributo default ou de Classe
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        #return f'Olá! {id(self)}'
        return f'Olá! meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 7

    @classmethod
    def nome_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Apeto de mão'

# Sobrescrita de atributo
class Mutane(Pessoa):
    olhos = 3



if __name__=='__main__':
    #guilherme = Pessoa(nome='Guilherme')
    #guilherme = Homem(nome='Guilherme')
    guilherme = Mutane(nome='Guilherme')
    gabriel = Pessoa(nome='Gabriel')
    #francisco = Pessoa(guilherme, gabriel, nome='Francisco')
    francisco = Homem(guilherme, gabriel, nome='Francisco')

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

    #Pessoa.olhos = 3

    print(Pessoa.olhos)
    print(francisco.olhos)
    print(guilherme.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(francisco.olhos), id(guilherme.olhos), id(gabriel.olhos))

    print(Pessoa.metodo_estatico(), francisco.metodo_estatico())

    print(Pessoa.nome_atributos_de_classe(), francisco.nome_atributos_de_classe())

    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(guilherme, Pessoa))
    print(isinstance(guilherme, Homem))
    print(guilherme.olhos)
    print(guilherme.cumprimentar())
    print(francisco.cumprimentar())