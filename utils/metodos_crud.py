from model.classes import Bicicleta
from utils.utilidades import incrementar_id_bike

bikes = list()


def cadastrar(modelo, cor, valor, nome_comprador, data_compra, nome_da_loja):
    bikes.append(Bicicleta(incrementar_id_bike(), modelo, cor, valor,  nome_comprador, data_compra, nome_da_loja))


def encontrar_bike(id_bike):
    retorno = ''
    for bicicleta in bikes:
        if bicicleta.id_bike == id_bike:
            retorno = bicicleta
            break
        else:
            retorno = None
    return retorno


def listando():
    for bicicleta in bikes:
        print(bicicleta.mostrar_bike())


def listar_bikes():
    if len(bikes) == 0:
        retorno = 'NÃO BIKES CADASTRADAS'
    else:
        listando()
        retorno = 'LISTADOS'
    return retorno


def listar_bike_por_id(id_bike):
    if len(bikes) == 0:
        saida = 'NÃO HÁ BIKES CADASTRADAS'
    else:
        bicicleta = encontrar_bike(id_bike)
        if type(bicicleta) == Bicicleta:
            saida = bicicleta
        else:
            saida = bicicleta
    return saida


def atualizar_bike(id_bike, modelo, cor, valor, comprador, data_compra, nome_loja):
    retorno = ''
    if len(bikes) == 0:
        retorno = 'NÃO HÁ BIKES CADASTRADAS.'
    else:
        bicicleta = encontrar_bike(id_bike)
        if type(bicicleta) == Bicicleta:
            bicicleta.set_modelo(modelo)
            bicicleta.set_cor(cor)
            bicicleta.set_valor(valor)
            bicicleta.set_nome_do_comprador(comprador)
            bicicleta.set_data_de_compra(data_compra)
            bicicleta.set_nome_da_loja(nome_loja)
        else:
            retorno = 'BIKE NÃO CADASTRADA.'
    return retorno


def deletar_bike(id_bike):
    if len(bikes) == 0:
        retorno = 'NÃO HÁ BIKES CADASTRADAS'
    else:
        bicicleta = encontrar_bike(id_bike)
        if type(bicicleta) == Bicicleta:
            bikes.remove(bicicleta)
            retorno = 'BIKE REMOVIDA COM SUCESSO'
        else:
            retorno = 'BIKE NÃO CADASTRADA'
    return retorno
