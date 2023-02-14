from model.classes import Bicicleta
from utilidades import validar_entrada_ponto_flutuante, incrementar_id_bike, validar_entrada_inteira

bikes = list()


def cadastrar():
    print('INFORME O MODELO DA BIKE: ')
    modelo = input('---> ')
    print('INFORME A COR DA BIKE: ')
    cor = input('---> ')
    print('INFORME O VALOR DA BIKE: R$')
    valor = validar_entrada_ponto_flutuante()
    print('INFORME O NOME DO COMPRADOR: ')
    nome_comprador = input('---> ')
    print('INFORME A DATA DE COMPRA DA BIKE: ')
    data = input('---> ')
    print('INFORME O NOME DA LOJA: ')
    nome_da_loja = input('---> ')

    bike = Bicicleta(incrementar_id_bike(), modelo, cor, valor,
                     nome_comprador, data, nome_da_loja)
    bikes.append(bike)


def listar_bikes():
    if len(bikes) == 0:
        print('NÃO BIKES CADASTRADAS')
    else:
        for bike in bikes:
            print(bike.mostrar_bike())


def listar_bike_por_id():
    retorno = ''
    if len(bikes) == 0:
        retorno = 'NÃO HÁ BIKES CADASTRADAS'
    else:
        print('INFORME O ID DA BIKE: ')
        id1 = validar_entrada_inteira()
        for bicicleta in bikes:
            if bicicleta.id_bike == id1:
                retorno = bicicleta.mostrar_bike()
                break
            elif bicicleta.id_bike != id1:
                retorno = 'BIKE NÃO CADASTRADA'

    return retorno

