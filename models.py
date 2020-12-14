import random


class Casas:
    corvinal = 'Corvinal'
    sonserina = 'Sonserina'
    lufalufa = 'Lufa-lufa'
    grifinoria = 'Grifinória'

    @staticmethod
    def lista_casas():
        return [Casas.corvinal, Casas.sonserina, Casas.lufalufa, Casas.grifinoria]


class Estudante:

    def __init__(self, nome, data_nascimento, ano=1, ativo=True):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.casa = None
        self.ano = ano
        self.ativo = ativo

    def subir_ano(self):
        if self.ano < 7:
            self.ano += 1

    # quando um estudante é graduado ele sai da escola e deixa de ser ativo
    def graduar(self):
        if self.ano == 7:
            self.ativo = False
            return 'Parabéns pela sua graduação pela Escola de Magia e Bruxaria de Hogwarts! Sentiremos sua falta.'

        return 'Você ainda é jovem demais para se graduar. Estude mais um pouco.'

    def chapeu_seletor(self):

        # sorteia um valor entre 0 e 3
        chapeu_resposta = random.randint(0, 3)

        # o valor sorteado pega a posição da lista
        casa_selecionada = Casas.lista_casas()[chapeu_resposta]
        self.casa = casa_selecionada

        return self.casa.upper() + ' !!!'



