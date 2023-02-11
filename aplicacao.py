from menus.menus import mostrar_menu_principal
from utils.utils import validar_entrada_inteira
loop = 0

while loop == 0:
    option = 0
    while option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
        mostrar_menu_principal()

        print('INFORME SUA ESCOLHA: ')
        option = validar_entrada_inteira()

        if option == 1:
            print('CADASTRAR BIKE')

        elif option == 2:
            print('LISTAR TODAS AS BIKES')

        elif option == 3:
            print('LISTAR UMA BIKE POR ID')

        elif option == 4:
            print('ATUALIZAR UMA BIKE')

        elif option == 5:
            print('DELETAR UMA BIKE')

        elif option == 6:
            print('SAIR')
            print()
            print('ENCERRANDO')
            loop = 1
