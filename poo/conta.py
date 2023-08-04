
#O encapsulamento refere-se ao ato de tornar os atributos privados e permitir 
#seu acesso apenas por meio dos métodos da classe, usando o prefixo __

#Getters e setters são usados para proteger seus dados, especialmente na criação de classes. 
#Para cada instância de variável, um método getter retorna seu valor, 
#enquanto um método setter o define ou atualiza.

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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.destino(valor)

    @property # para getters
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter # para setters
    def limite(self, limite):
        self.__limite = limite

    @staticmethod #Metodos estaticos 
    def codigo_banco():
        return "001"