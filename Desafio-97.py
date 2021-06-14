#Faça programa que tenha uma função chamada escreva(),
#       que receba um texto qualquer e mostre uma mensagem
#       com tamanho adaptável
#Autora:Andressa Cristina Anthero

def escreva(frase):
    tam = len(frase) + 4
    print('~'*tam)
    print(f'  {frase}')
    print('~'*tam)


frase = str(input('Escreva a frase aqui: '))
escreva(frase)

