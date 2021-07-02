from dados.dados_registro import registra_analise_credito


def analisa_credito(cpf, idade, valor):
    print(" * Analise de credito sendo realizada, cliente CPF " + cpf)

    cpf_verificado = verifica_cpf(cpf)
    idade_verificada = verifica_idade(idade)
    valor_verificado = verifica_valor(valor)
    total = (cpf_verificado + idade_verificada + valor_verificado) / 3

    if not cpf_verificado or not idade_verificada or not valor_verificado:
        aprovacao = 'nao contemplado'
    else:
        aprovacao = 'aprovado'

    registra_analise_credito(cpf, idade, valor, total, aprovacao)
    return total, aprovacao





def verifica_cpf(cpf_cnpj):
    if len(cpf_cnpj) == 11:
        return 95
    elif len(cpf_cnpj) == 14:
        return 100
    else:
        return 0

def verifica_idade(idade):
    if idade < 18:
        return 0
    elif idade < 25:
        return 80
    elif idade < 40:
        return 90
    else:
        return 100

def verifica_valor(valor):
    if valor > 100000:
        return 0
    elif valor < 15000:
        return 100
    else:
        return 90