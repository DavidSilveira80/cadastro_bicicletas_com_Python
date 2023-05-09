from model.classes import Bicicleta
from utils.utilidades import validar_entrada_ponto_flutuante, incrementar_id_bike, validar_entrada_inteira

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


def atualizar_bike():
    retorno = ''
    if len(bikes) == 0:
      retorno = 'NÃO HÁ BIKES CADASTRADAS.'
    else:
        print('INFORME O ID DA BIKE: ')
        id1 = validar_entrada_inteira()
        for bike in bikes:
           if bike.id_bike == id1:
               print('INFORME MODELO')
               bike.modelo = input('----> ')
               print('INFORME A COR')
               bike.cor = input('----> ')
               print('INFORME VALOR')
               bike.valor = validar_entrada_ponto_flutuante()
               print('INFORME NOME DO COMPRADOR')
               bike.nome_do_comprador = input('----> ')
               print('INFORME DATA DA COMPRA')
               bike.data_da_compra = input('----> ')
               print('INFORME NOME DA LOJA')
               bike.nome_da_loja = input('----> ')
               retorno = 'BIKE ATUALIZADA COM SUCESSO'
           elif bike.id_bike != id1:
               retorno = 'BIKE NÃO CADASTRADA.'
    return retorno



