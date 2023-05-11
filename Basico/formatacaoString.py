print("Tentativa {} de {}".format(3,10))
print("Tentativa {1} de {0}".format(3,10)) # parâmetros podem ser invertidos na string
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))

print("-----------------------------")
print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59)) # formatacao de float
print("R$ {:.2f}".format(1.59))

print("-----------------------------")
# ponto fique sempre no mesmo local
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))
print("R$ {:07.2f}".format(1.5)) #preencher os espaços em branco com zeros

print("-----------------------------")
print("R$ {:07d}".format(4)) #formatar números inteiros
print("Data {:02d}/{:02d}".format(9, 4)) #formatar uma data
print("Data {:02d}/{:02d}".format(19, 11)) #formatar uma data

print("-----------------------------")
print("Coordinates: {latitude}, {longitude}".format(latitude='37.24N', longitude='-115.81W')) #Acessando argumentos por nome
coord = (3, 5)
print("X: {0[0]};  Y: {0[1]}".format(coord))