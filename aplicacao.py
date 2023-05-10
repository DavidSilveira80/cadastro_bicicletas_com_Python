from menus.menus import mostrar_menu_principal
from utils.metodos_crud import cadastrar, listar_bikes, listar_bike_por_id, atualizar_bike, deletar_bike
from utils.utilidades import validar_entrada_inteira, validar_entrada_ponto_flutuante

loop = 0
while loop == 0:
    option = 0
    while option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
        mostrar_menu_principal()

        print('INFORME SUA ESCOLHA: ')
        option = validar_entrada_inteira()

        if option == 1:
            print('CADASTRAR BIKE')
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
            cadastrar(modelo, cor, valor, nome_comprador, data, nome_da_loja)

        elif option == 2:
            print('LISTAR BIKES')
            listar_bikes()

        elif option == 3:
            print('LISTAR UMA BIKE POR ID')
            print('INFORME O ID DA BIKE: ')
            print(listar_bike_por_id(validar_entrada_inteira()))

        elif option == 4:
            print('ATUALIZAR UMA BIKE')
            print('INFORME O ID DA BIKE: ')
            id_bike = validar_entrada_inteira()
            modelo = input('INFORME MODELO:----> ')
            cor = input('INFORME A COR:----> ')
            print('INFORME VALOR:----> ')
            valor = validar_entrada_ponto_flutuante()
            nome_do_comprador = input('INFORME NOME DO COMPRADOR:----> ')
            data_da_compra = input('INFORME DATA DA COMPRA:----> ')
            nome_da_loja = input('INFORME NOME DA LOJA:----> ')
            print(atualizar_bike(id_bike, modelo, cor, valor, nome_do_comprador, data_da_compra,
                                 nome_da_loja))

        elif option == 5:
            print('DELETAR UMA BIKE')
            print('INFORME O ID DA BIKE: ')
            print(deletar_bike(validar_entrada_inteira()))

        elif option == 6:
            print('SAIR')
            print()
            print('ENCERRANDO')
            loop = 1
