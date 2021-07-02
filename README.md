# API_Flask-Celery

#PARA RODAR A API
- Ative o Redis na porta 6379
- Acione o Worker do Celery no main a partir do comando "celery -A main.celery worker"
- Execute o servidor Flask pelo arquivo main.py


#ROTAS DA API
- "../credito/"
Essa é uma rota do tipo POST que está preparada para receber idade, valor e cpf, como no modelo:
{
    "idade":63,
    "valor":60000,
    "cpf": "9647959541"
}

Ela processo o pedido de maneira ASSINCRONA, devolvendo imediatamento um ticket como resposta.


-"../resposta-credito/
Essa é uma rota do tipo GET que recebe o TICKET como parâmetro na url e devolve o processamento requerido na rota anterior.
Enquanto o resultado do processamento não é entregue, a rota devolve PENDING como resposta.
