# Para imprimir 
# print("Brasil ganhou 5 titulos mundiais")

# o sep defini o que deve fazer entre esses 4 valores que foi passado no print
# print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")

# end defini o que vai ser colocado no final do print (colocando \n ele faz a quebra de linha)
# print("Brasil", "ganhou", 5, "titulos mundiais", end="-")

# Variaveis (Não é preciso declarar o tipo (String/Double/Int))
# Exemplo 1 com variaveis
br = "brasil"
it = "italia"
placarBr = 3
placarIt = 2
print ("O", br, "ganhou da", it, "de", placarBr, "x", placarIt, "no campeonato.")

# Exemplo 2 com variaveis e sep/end
subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")

# Exemplo 3
dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep='/')

# Concatenação
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)

# Vai imprimir 10 vezes o numero 20 na mesma linha
numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)