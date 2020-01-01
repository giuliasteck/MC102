"""
Nome: Giulia Steck
RA: 173458
"""

lista =[]

N = int(input())
for i in range(N):
    entrada = input()
    lista.append(entrada)

hashtag = 0
emoticon = 0

for i in (lista):
    a = i.isdigit()
    b = i.isalpha()

    #printar números positivos e palavras
    if a == True:
        print(i)
    elif b == True:
        print(i)

    #printar números negativos
    elif i[0] == '-':
        checarNumero = i[1:]
        cN = checarNumero.isdigit()
        if cN == True:
            print(i)
        else:
            emoticon += 1
    
    #checar hashtags e emoticons
    elif i[0] == '#':
        checarPalavra = i[1:]
        cP = checarPalavra.isalpha()
        if cP == True:
            hashtag += 1
        elif cP == False:
            emoticon += 1
    else:
        emoticon += 1


if hashtag > 1:
    print (hashtag,'hashtags foram removidas.')
elif hashtag == 1:
        print (hashtag,'hashtag foi removida.')

if emoticon > 1:
    print (emoticon,'emoticons foram removidos.')
elif emoticon == 1:
    print (emoticon,'emoticon foi removido.')

