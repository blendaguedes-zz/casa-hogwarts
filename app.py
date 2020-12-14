from flask import Flask, request
import validacao

app = Flask(__name__)


@app.route('/')
def index():

    return 'Bem vindos a Escola de Magia e Bruxaria de Hogwarts!'


@app.route('/matricula', methods=['POST'])
def matricula():

    estudante = request.json

    resultado_matricula = validacao.matricula_validacao(estudante)

    return resultado_matricula


@app.route('/subirdeano', methods=['PUT'])
def subir_ano():

    estudante_id = request.json
    resultado_subir_ano = validacao.subir_ano_validacao(estudante_id)

    return resultado_subir_ano


@app.route('/graduacao', methods=['PUT'])
def graduar():

    estudante_id = request.json
    resultado_graduacao = validacao.graduar_validacao(estudante_id)

    return resultado_graduacao


if __name__ == '__main__':
    app.debug = True
    app.run()
