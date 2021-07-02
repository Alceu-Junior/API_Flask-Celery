from flask import Flask, request, jsonify
import celery.states as states

from monta_celery.make_celery import make_celery
from dominio.regras_negocio import analisa_credito
from dados.dados_registro import registra_pedido


app = Flask(__name__)
try:
    app.config['CELERY_BROKER_URL'] =  'redis://localhost:6379'
    app.config['CELERY_RESULT_BACKEND'] =  'redis://localhost:6379'
    celery = make_celery(app)
except:
    print(' * Por favor, verifique se o Redis e o Celery foram inicializados e se a porta está correta antes de rodar o programa')


@app.route('/credito', methods=['POST'])
def credito():
    data = request.get_json(force=True)
    cpf = data['cpf']
    idade = data['idade']
    valor = data['valor']    
    print(' * Pedido de credito recebido de CPF - ' + cpf)

    try:
        task = verifica_credito.delay(cpf, idade, valor)
        registra_pedido(task.id, cpf, idade, valor)
    except:
        registra_pedido('RETORNAR CONTATO', cpf, idade, valor)
        print(" * Verifique o funcionamento do Celery, dados do cliente nao atendido registrados com a task.id 'RETORNAR CONTATO'")

    return task.id, 201


@celery.task(name='tasks.verifica_credito')
def verifica_credito(cpf, idade, valor):
    print(' * Pedido de credito encaminhado para verificacao, cliente ' + cpf)
    total, aprovacao = analisa_credito(cpf, idade, valor)
    return {
        'aprovacao' : aprovacao,
        'cpf' : cpf,
        'idade' : idade,
        'valor' : valor,
        'score' : total
    }

@app.route('/resposta-credito/<ticket>')
def resposta_credito(ticket):
    resposta = celery.AsyncResult(ticket)
    if resposta.state == states.PENDING:
        print(" * Resposta de credito solicitada, ainda pendente, ticket " + ticket)
        return resposta.state, 202
    else:
        print(" * Sucesso, resposta de credito entregue ao ticket " + ticket)
        return jsonify(resposta.result)




if __name__ == '__main__':
    app.run(debug=True)