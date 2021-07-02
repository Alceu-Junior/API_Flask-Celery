from datetime import datetime

arquivo_pedidos ='registro_pedidos.txt'
arquivo_analise = 'registro_analise_credito.txt'


def registra_pedido(ticket, cpf, idade, valor):    
    try:
        arquivo = open(arquivo_pedidos,'a')
        arquivo.write(str(datetime.now()) + ',' + str(ticket) + ',' + str(cpf) + ',' + str(idade) + ',' + str(valor) + "\n")
        print(" * Gravacao de dados concluida. - Arquivo " + arquivo.name)
    except:
        print("Algo de errado na gravacao do arquivo " + arquivo.name)
    finally:
        arquivo.close()


def registra_analise_credito(cpf, idade, valor, score, aprovacao):
    try:
        arquivo = open(arquivo_analise, 'a')
        arquivo.write(str(datetime.now()) + ',' + str(cpf) + ',' + str(idade) + ',' + str(valor) + ',' + str(score) + ',' + str(aprovacao) + "\n")
        print(" * Gravacao de dados concluida. - Arquivo " + arquivo.name)
    except:
        print("Algo de errado na gravacao do arquivo " + arquivo.name)    
    
    finally:
        arquivo.close()

  