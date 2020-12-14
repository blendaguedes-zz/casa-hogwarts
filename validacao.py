import datetime
from models import Estudante
import bd


# verificar se a data está no formato certo
def data_validacao(data_nascimento):
    dia, mes, ano = data_nascimento.split('-')

    # try é utilizado para testar um bloco de código
    try:
        datetime.datetime(int(ano), int(mes), int(dia))
        return data_nascimento

    # se o bloco dentro do try der errado o bloco except é executado
    except ValueError:
        return False


def ano_validacao(ano):
    if ano is int:
        if 1 <= ano < 8:
            return True

    return False


def matricula_validacao(dados_matricula):
    try:
        nome = dados_matricula['nome']
        data_nascimento = dados_matricula['data nascimento']

        if data_validacao(data_nascimento):
            novo_estudante = Estudante(nome, data_nascimento)

            chapeu = novo_estudante.chapeu_seletor()

            dados_matricula = list(novo_estudante.__dict__.values())
            print(dados_matricula)

            bd.inserir_dado(dados_matricula)

            return chapeu
    except ValueError:
        return 'Data de nascimento inválida. Estudante não cadastrado'


def subir_ano_validacao(dados_estudante):
    try:
        id_estudante = dados_estudante['id']

        dados_estudante['nome'], \
        dados_estudante['data_nascimento'], \
        dados_estudante['ano'], \
        dados_estudante['ativo'] = bd.pegar_dado_id(id_estudante)

        if dados_estudante['ativo']:
            estudante = Estudante(dados_estudante['nome'], dados_estudante['data_nascimento'],
                                  dados_estudante['ano'], dados_estudante['ativo'])

            estudante.subir_ano()

            bd.alterar_dado((estudante.ano, estudante.ativo, id_estudante))

            return 'Parabéns! Você subiu para o ' + str(estudante.ano) + '!!!'
        return 'Estudante inativo.'

    except:

        return 'Você não pode subir de ano!'


def graduar_validacao(dados_estudante):
    try:
        id_estudante = dados_estudante['id']

        dados_estudante['nome'], dados_estudante['data_nascimento'], dados_estudante['ano'], \
        dados_estudante['ativo'] = bd.pegar_dado_id(id_estudante)

        if dados_estudante['ativo']:
            estudante = Estudante(dados_estudante['nome'], dados_estudante['data_nascimento'],
                                  dados_estudante['ano'], dados_estudante['ativo'])

            resultado_graduacao = estudante.graduar()
            bd.alterar_dado((estudante.ano, estudante.ativo, id_estudante))

            return resultado_graduacao
        return 'Você provavelmente já é graduado. (Ou foi expulso).'

    except:
        # tratamento de erro para usuário. Esse tipo de problema pode ser mapeado no
        return 'Erro do servidor interno da operação. O erro foi reportado, por favor aguarde e tente mais tarde.'
