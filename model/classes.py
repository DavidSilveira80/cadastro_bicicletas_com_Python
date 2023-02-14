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

        return f'----------------------------------------------\n'\
               f'Id da bike: {self.id_bike}\nModelo da bike: {self.modelo}\n'\
               f'Cor da bike: {self.cor}\nNome do comprador: '\
               f'{self.nome_do_comprador}\nData da compra: '\
               f'{self.data_de_compra}\nNome da loja: {self.nome_da_loja}'
