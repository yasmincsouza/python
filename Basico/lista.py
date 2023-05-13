valores = [] # como é criado a lista
print(type(valores))

valores = [0,1,2,3,4]
print(min(valores)) #valor minimo
print(max(valores)) #valor maximo
print(valores[3]) #retorna o valor pelo indice
print(len(valores))

# tuple é uma lista imutável
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado") # como é criado uma tupla
print(type(dias))
# dias.append("Sábado2") # não é possivel adicionar, nem remover elementos.

pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)
instrutores = [pessoa1, pessoa2, pessoa3]
print(instrutores)
print(instrutores[1][1]) # para saber a idade do Flavio

# dictionary
instrutores = {'Nico' : 39, 
               'Flavio': 37, 
               'Marcos' : 30}
print(instrutores['Flavio'])

# set não pode existir elementos duplicados. 
# set não é uma sequência, pois não tem um índice
colecao = {11122233344, 22233344455, 33344455566} # como é criado um set
colecao.add(44455566677) #vai adicionar pois não existe ainda
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!