import sqlite3


def conecte():
    conexao = sqlite3.connect("hogwarts.sqlite")
    cursor = conexao.cursor()
    return conexao, cursor


def criar_tabela():
    conexao, cursor = conecte()

    comando_sql = "CREATE TABLE estudante(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                  "nome TEXT NOT NULL, data_nascimento NOT NULL, casa TEXT NOT NULL, " \
                  "ano INTEGER NOT NULL, ativo INTEGER NOT NULL)"

    cursor.execute(comando_sql)
    conexao.close()


def inserir_dado(dado):
    conexao, cursor = conecte()

    comando_sql = "INSERT INTO estudante(nome, data_nascimento, casa, ano, ativo) values (?, ?, ?, ?, ?)"

    cursor.execute(comando_sql, dado)
    conexao.commit()
    conexao.close()


def inserir_multiplos_dados(dados):
    conexao, cursor = conecte()

    comando_sql = "INSERT INTO estudante(nome, data_nascimento, casa, ano) values (?, ?, ?, ?)"

    cursor.executemany(comando_sql, dados)
    conexao.commit()
    conexao.close()


# esse método servirá para alterar o ano e se o estudante está ativo.
def alterar_dado(dado):
    conexao, cursor = conecte()

    comando_sql = "UPDATE estudante SET ano = ?, ativo = ? WHERE id = ?"

    cursor.execute(comando_sql, dado)
    conexao.commit()
    conexao.close()


def pegar_dado_id(dado_id):
    conexao, cursor = conecte()

    comando_sql = "SELECT nome,  data_nascimento, ano, ativo FROM estudante WHERE id = :id"

    resposta = cursor.execute(comando_sql, {'id': dado_id}).fetchone()

    return resposta
