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

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_cor(self, cor):
        self.cor = cor

    def set_valor(self, valor):
        self.valor = valor

    def set_nome_do_comprador(self, nome):
        self.nome_do_comprador = nome

    def set_data_de_compra(self, data_compra):
        self.data_de_compra = data_compra

    def set_nome_da_loja(self, nome_loja):
        self.nome_da_loja = nome_loja

    def mostrar_bike(self):

        return f'----------------------------------------------\n'\
               f'Id da bike: {self.id_bike}\nModelo da bike: {self.modelo}\n'\
               f'Cor da bike: {self.cor}\nNome do comprador: '\
               f'{self.nome_do_comprador}\nData da compra: '\
               f'{self.data_de_compra}\nNome da loja: {self.nome_da_loja}'
