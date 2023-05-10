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


def encontrar_bike(id):
    for bike in bikes:
        if bike.id_bike == id:
            retorno = bike
            break
        else:
            retorno = 'BIKE NÃO CADASTRADA.'
    return retorno


def listar_bikes():
    if len(bikes) == 0:
        print('NÃO BIKES CADASTRADAS')
    else:
        for bike in bikes:
            print(bike.mostrar_bike())


def listar_bike_por_id():
    if len(bikes) == 0:
        retorno = 'NÃO HÁ BIKES CADASTRADAS'
    else:
        print('INFORME O ID DA BIKE: ')
        id1 = validar_entrada_inteira()
        retorno = encontrar_bike(id1)
        if type(retorno) == Bicicleta:
            retorno = retorno.mostrar_bike()
    return retorno


def atualizar_bike():
    if len(bikes) == 0:
      retorno = 'NÃO HÁ BIKES CADASTRADAS.'
    else:
        print('INFORME O ID DA BIKE: ')
        id1 = validar_entrada_inteira()
        retorno = encontrar_bike(id1)
        if type(retorno) == Bicicleta:
               print('INFORME MODELO')
               retorno.modelo = input('----> ')
               print('INFORME A COR')
               retorno.cor = input('----> ')
               print('INFORME VALOR')
               retorno.valor = validar_entrada_ponto_flutuante()
               print('INFORME NOME DO COMPRADOR')
               retorno.nome_do_comprador = input('----> ')
               print('INFORME DATA DA COMPRA')
               retorno.data_da_compra = input('----> ')
               print('INFORME NOME DA LOJA')
               retorno.nome_da_loja = input('----> ')
               print('BIKE ATUALIZADA COM SUCESSO')
        else:
          retorno = retorno
    return retorno


def deletar_bike():
    if len(bikes) == 0:
        print('NÃO HÁ BIKES CADASTRADAS')
    else:
        print('INFORME O ID DA BIKE: ')
        id1 = validar_entrada_inteira()
        retorno = encontrar_bike(id1)
        if type(retorno) == Bicicleta:
            bikes.remove(retorno)
            print('BIKE REMOVIDA COM SUCESSO')
        else:
            print('BIKE NÃO CADASTRADA')
