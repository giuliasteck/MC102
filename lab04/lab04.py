'''
Giulia Steck - RA:173458
Entrada: notas mínimas para ganhar um certo tipo
de medalha e nota de cada participante até ser 
inserido o -1
Saída: quantos atletas ganharam cada medalha, calculado
por meio de uma variável somadora e a maior nota obtida.
'''

medalhaOuro = float(input())
medalhaPrata = float(input())
medalhaBronze = float(input())

"{:.1f}".format(medalhaOuro)
"{:.1f}".format(medalhaPrata)
"{:.1f}".format(medalhaBronze)

#Notas dos participantes
nota = float(input())
"{:.1f}".format(nota)
notas = []
notas.append(nota)
print(notas)

#Criação da lista com notas dos participantes
while nota != -1:
    nota=float(input())
    "{:.1f}".format(nota)
    if nota != -1:
        notas.append(nota)
    elif nota == -1:
        break
print(notas)

ouro = 0
prata = 0
bronze = 0
for i in (notas):
    if i>=medalhaOuro:
        ouro += 1
    elif i >= medalhaPrata and i<medalhaOuro:
        prata += 1
    elif i >= medalhaBronze and i<medalhaPrata:
        bronze += 1

if ouro >= 1:
    print ('Medalha(s) de ouro:',ouro)
else:
    print('Nenhum participante recebeu medalha de ouro!')

if prata>=1:
    print
    print ('Medalha(s) de prata:',prata)
else:
    print('Nenhum participante recebeu medalha de prata!')

if bronze>=1:
    print ('Medalha(s) de bronze:',bronze)
else:
    print('Nenhum participante recebeu medalha de bronze!')

maiorNota = max(notas)
print('Maior nota:',maiorNota)


