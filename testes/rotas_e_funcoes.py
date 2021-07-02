import requests

dados_cliente = {
    "idade": 0000,
    "valor": 0000,
    "cpf": "teste"
}

requisicao_credito = 'http://localhost:5000//credito'
resposta_ticket = 'http://localhost:5000//resposta-credito/'

def post(url, data):
    res = requests.post(url, json=data)
    return res

def get(url):
    res = requests.get(url)
    return res