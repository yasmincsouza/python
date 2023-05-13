arquivo = open("palavras.txt", "w") # cria um arquivo
print(arquivo.write("banana\n"))
print(arquivo.write("melancia\n"))
arquivo.close()

arquivo = open("palavras.txt", "a")
print(arquivo.write("morango\n"))
print(arquivo.write("manga\n"))

