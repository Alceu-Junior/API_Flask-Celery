from time import sleep
from rotas_e_funcoes import dados_cliente, requisicao_credito, resposta_ticket, post, get

ticket = post(requisicao_credito, dados_cliente)
print(ticket.status_code)
if ticket.status_code >= 200 and ticket.status_code < 300:
    print('Rota POST para pedido de credito funcionando')
else:
    print('***problemas com a rota POST de pedido de credito')

sleep(2)

resposta_analise = get(resposta_ticket + ticket.text)
print(resposta_analise.status_code)
if resposta_analise.status_code >= 200 and resposta_analise.status_code < 300:
    print('Rota GET para resposta de pedido de credito com ticket funcionando')
else:
    print('***problemas com a rota GET para resposta de pedido de credito com ticket')
