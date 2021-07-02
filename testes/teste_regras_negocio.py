from dominio.regras_negocio import verifica_cpf, verifica_idade, verifica_valor, analisa_credito


### Teste da função verifica_cpf()
if verifica_cpf(12345678901) == 95:
    print("'verifica_cpf()' retorna 95 pontos caso cpf tenha 11 numeros")
if verifica_cpf(12345678901234) == 100:
    print("'verifica_cpf()' retorna 100 pontos caso cpf seja um cnpj, tenha 14 numeros")
if verifica_cpf(1234567890) == 0:
    print("'verifica_cpf()' retorna 0 pontos caso tenha menos de 11 digitos")
if verifica_cpf(123456789012345) == 0:
    print("'verifica_cpf()' retorna 0 pontos caso tenha mais de 14 digitos")

### Teste da função verifica_idade()
if verifica_idade(17) == 0:
    print("'verifica_idade()' retorna 0 pontos caso idade seja menor que 18")
else:
    print("***problema na função 'verifica_idade()'")
if verifica_idade(24) == 80:
    print("'verifica_idade()' retorna 80 pontos caso idade seja maior que 18 e menor que 25")
else:
    print("***problema na função 'verifica_idade()'")
if verifica_idade(39) == 90:
    print("'verifica_idade()' retorna 90 pontos caso idade seja maior que 25 e menor que 40")
else:
    print("***problema na função 'verifica_idade()'")
if verifica_idade(41) == 100:
    print("'verifica_idade()' retorna 100 pontos caso idade seja maior que 40")
else:
    print("***problema na função 'verifica_idade()'")


### Teste da função verifica_valor()
if verifica_valor(100001) == 0:
    print("'verifica_valor()' retorna 0 pontos caso valor seja maior que $100.000,00")
else:
    print("***problema na função 'verifica_valor()'")
if verifica_valor(14999) == 100:
    print("'verifica_valor()' retorna 100 pontos caso valor seja menor que $15.000,00")
else:
    print("***problema na função 'verifica_valor()'")
if verifica_valor(50000) == 90:
        print("'verifica_valor()' retorna 90 pontos caso valor seja entre $15.000,00 e $100.000,00")
else:
    print("***problema na função 'verifica_valor()'")


### Teste da função analisa_credito()
if analisa_credito(1234567, 25, 5000) == 'nao contemplado':
    print("'analisa_credito()' retorna 'nao contemplado' se parametro 'cpf' for invalido")
else:
    print("***problema na função 'analisa_credito()'")

if analisa_credito(12345678901, 15, 5000) == 'nao contemplado':
    print("'analisa_credito()' retorna 'nao contemplado' se parametro 'idade' for invalido")
else:
    print("***problema na função 'analisa_credito()'")

if analisa_credito(12345678901, 25, 500000000) == 'nao contemplado':
    print("'analisa_credito()' retorna 'nao contemplado' se parametro 'valor' for invalido")
else:
    print("***problema na função 'analisa_credito()'")

if analisa_credito(12345678901, 25, 5000) == 'aprovado':
    print("'analisa_credito()' retorna 'aprovado' se os parametros 'cpf', 'idade' e 'valor' forem validos")
else:
    print("***problema na função 'analisa_credito()'")