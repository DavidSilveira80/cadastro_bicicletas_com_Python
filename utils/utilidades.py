contador = 0


def incrementar_id_bike():
    global contador
    contador += 1
    return contador


def validar_entrada_inteira():
    continua_leitura = True
    entrada = 0
    while continua_leitura:
        try:
            entrada = int(input('---> '))
            continua_leitura = False
        except ValueError:
            print('ENTRADA COM VALOR INVÁLIDO. TENTE NOVAMENTE')
            print('INFORME SUA ESCOLHA')

    return entrada


def validar_entrada_ponto_flutuante():
    continua_leitura = True
    entrada = 0.0
    while continua_leitura:
        try:
            entrada = float(input('---> '))
            continua_leitura = False
        except ValueError:
            print('ENTRADA COM VALOR INVÁLIDO. TENTE NOVAMENTE')
            print('INFORME SUA ESCOLHA')

    return entrada
