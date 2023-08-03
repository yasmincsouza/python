
class Conta:
    #Função construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        #Atributos
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #Metodos
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor