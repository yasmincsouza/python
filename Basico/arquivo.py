# w é para escrita / r é para leitura / a para adicionar a um arquivo pré existente
arquivo = open("palavras.txt", "w") # cria um arquivo
print(arquivo.write("banana\n"))
print(arquivo.write("melancia\n"))
arquivo.close()

# arquivo = open("palavras.txt", "a")
print(arquivo.write("morango\n"))
print(arquivo.write("manga\n"))

# o modificador b que devemos utilizar quando queremos 
# trabalhar no modo binário. Para abrir uma imagem devemos usar
# imagem = open("foto.jpg", "rb")

# arquivo copia.py
# cria uma cópia de uma imagem
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()