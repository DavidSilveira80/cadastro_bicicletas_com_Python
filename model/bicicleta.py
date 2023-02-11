class Bicicleta:

    # Método construtor
    def __init__(self, id_bike, modelo, cor, valor, nome_do_comprador, data_de_compra, nome_da_loja):
        self.id_bike = id_bike
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.nome_do_comprador = nome_do_comprador
        self.data_de_compra = data_de_compra
        self.nome_da_loja = nome_da_loja

    def mostrar_bike(self):
        print()
        print(f'Id da bike: {self.id_bike}')
        print(f'Modelo da bike: {self.modelo}')
        print(f'Cor da bike: {self.cor}')
        print(f'Nome do comprador: {self.nome_do_comprador}')
        print(f'Data da compra: {self.data_de_compra}')
        print(f'Nome da loja: {self.nome_da_loja}')





