
#O encapsulamento refere-se ao ato de tornar os atributos privados e permitir 
#seu acesso apenas por meio dos métodos da classe, usando o prefixo __

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

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.destino(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite