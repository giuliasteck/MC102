from forca import lista_palavras, cenas_forca
escolha = int(input("Escolha um número entre 0 e 49: "))

palavra = 0
if escolha > 49:
    print("Numero Invalido")
    quit()
else:
    palavra = lista_palavras[escolha]

#Separa cada letra da palavra em um novo item da lista
listaPalavra = list(palavra)

#Lista com os tracinhos
tentativas = ["_" for i in range (len(listaPalavra))]

"""
#Primeira imagem mostrada
print (cenas_forca[0])
#Printar a progressão do jogo
print('Palavra:', end = ' ')
print(*tentativas, sep='  ')
"""

letra = 0
letrasErradas = []
erros = 0

while erros < 6:
    #Primeira imagem mostrada
    print (cenas_forca[erros])
    #Printar a progressão do jogo
    print('Palavra:', end = ' ')
    print(*tentativas, sep='  ')
    if len(letrasErradas) != 0:
        print('Tentativa(s) incorreta(s):',*letrasErradas,sep = ' ')

    letra = input('Proxima letra: ') 
    
    if letra in(listaPalavra):
        for i in range(len(lista_palavras[escolha])):
            if listaPalavra[i] == letra:
                tentativas[i] = letra
        if listaPalavra == tentativas:
            print('Palavra encontrada!')
            break

    else:
        if letra in letrasErradas:
            erros = erros
            print ('Proxima letra: Voce jah escolheu esta letra.')
        else:
            erros += 1
            letrasErradas.append(letra)

if erros >= 6:
    print('Palavra oculta:', lista_palavras[escolha])
