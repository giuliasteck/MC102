from forca import lista_palavras, cenas_forca

escolha = int(input('Escolha um numero entre 0 e 49: '))

if escolha < 50:
    erros = 0
    letrasErradas = []
    palavra = list(lista_palavras[escolha])
    tentativas = ["_" for i in range (len(palavra))]
    while erros <= 6:
        print('')
        print(cenas_forca[erros])
        print('Palavra:', end=' ')
        print(*tentativas, sep = '  ')
        if erros >= 1:
            print('Tentativa(s) incorreta(s):',*letrasErradas)
        if palavra == tentativas:
            print('Palavra encontrada!')
            break

        if erros == 6:
            print('Palavra oculta:', lista_palavras[escolha])
            break
        letra = input('Proxima letra: ')

        if letra in tentativas:
            print('Voce jah escolheu esta letra.')

        if letra in letrasErradas:
            print('Voce jah escolheu esta letra.')

        if letra not in letrasErradas and letra not in palavra:
            erros += 1
            letrasErradas.append(letra)
        
        for i in range(len(lista_palavras[escolha])):
            if palavra[i] == letra:
                tentativas[i] = letra
else:
    print('Numero invalido.')
