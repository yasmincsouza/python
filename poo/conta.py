
class Conta:
    # Função construtora
    # Self funciona como referencia
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        # Atributos publicos
        #self.numero = numero
        #self.titular = titular
        #self.saldo = saldo
        #self.limite = limite

        # Atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Metodos
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor