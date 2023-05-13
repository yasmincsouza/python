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
dias.append("Sábado2") # não é possivel adicionar, nem remover elementos.