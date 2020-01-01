cartelaBingo = []

for i in range(5):
    numero = input()
    linha = numero.split(' ')
    cartelaBingo.append(linha)


print('+----------------+')
print('| B  I  N  G  O  |')
print('+================+')

for i in cartelaBingo:
    print('|', end = ' ')
    print(*i, end=' ')
    print('|')

print('+----------------+')

quantidade = int(input())

for i in range(quantidade):
    sorteado = input()
    numerosChamados = sorteado.split('-')
    print(sorteado)
    for j in range(5):
        for k in range(5):
            if cartelaBingo[j][k] == numerosChamados[1]:
                cartelaBingo[j][k] = 'XX'

                print('+----------------+')
                print('| B  I  N  G  O  |')
                print('+================+')

                for i in cartelaBingo:
                    print('|', end = ' ')
                    print(*i, end=' ')
                    print('|')
                print('+----------------+')

    for i in range(5):
        #checar linhas
        if cartelaBingo[i][0] == 'XX' and cartelaBingo[i][1] == 'XX' and cartelaBingo[i][2] == 'XX' and cartelaBingo[i][3] == 'XX' and cartelaBingo[i][4] == 'XX':
            print('BINGO!')
            quit()

        #checar colunas
        elif cartelaBingo[0][i] == 'XX' and cartelaBingo[1][i] == 'XX' and cartelaBingo[2][i] == 'XX' and cartelaBingo[3][i] == 'XX' and cartelaBingo[4][i] == 'XX' and cartelaBingo[4][i] == 'XX':
            print('BINGO!')
            quit()

        #checar diagonais
        elif cartelaBingo[0][0] == 'XX' and cartelaBingo[1][1] == 'XX' and cartelaBingo[2][2] == 'XX' and cartelaBingo[3][3] == 'XX' and cartelaBingo[4][4] == 'XX':
            print('BINGO!')
            quit()

        elif cartelaBingo[0][4] == 'XX' and cartelaBingo[1][3] == 'XX' and cartelaBingo[2][2] == 'XX' and cartelaBingo[3][1] == 'XX' and cartelaBingo[4][0] == 'XX':
            print('BINGO!')
            quit()
