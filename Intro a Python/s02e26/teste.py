# texto = '''
# sdfasdfasdfasdf
# asdfasdfasdfasdf
# asdfasfdasdfasdf
# '''

 # w = write, r = read, a = escrita preservando o antigo w+b wscrita no modo binario
with open('arquivo.txt', 'r') as arq:
    lista = arq.read()

print(len(lista))