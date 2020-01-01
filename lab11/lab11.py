num = input()

print('Elemento procurado:', num)

num = num.zfill(3)
print(num)

inteiros = input()
lista = inteiros.split(' ')
numeros = []

for i in lista:
    i = i.zfill(3)
    numeros.append(i)

print(numeros)

for i in (numeros):
    if i == numeros[0]:
        print('+-----+', end = '')
    elif i == numeros[-1]:
        print('-----+')
    else:
        print('-----+', end = '')

for i in (numeros):
    if i == numeros[0]:
        print('|', end=' ')
        print(i, end = ' ')
        print('|',end = '')
    elif i== numeros[-1]:
        print(' ', end='')
        print(i, end = ' ')
        print('|')    
    else:
        print(' ', end='')
        print(i, end = ' ')
        print('|', end = '')

for i in (numeros):
    if i == numeros[0]:
        print('+-----+', end = '')
    elif i == numeros[-1]:
        print('-----+')
    else:
        print('-----+', end = '')
