"""
Nome: Giulia Steck 
RA: 173458
Descrição: esse programa tem como objetivo criar um banco de dados e,
a partir dele, calcular a taxa média do aumento do Poder de Combate das
espécies de pokémons presentes nesse banco de dado a partir da divisão do
Poder de combate após a evolução pelo Poder de Combate anterior a ela.
Como saida, o programa printa a estimativa da Poder de Combate final de
uma espécie presente no banco de dados a partir da multiplicação do Poder
de Combate inicial pela taxa média encontrada no banco de dados.
"""
import math

N = int(input())

bancoDados = [] #criação de uma lista vazia que será incrementada no for loop

for i in range (N):
    #entrada do número da espécie, do seu Poder de Combate inicial e final
    especie, PCa, PCf = input().split() 
    #indicação de que as entradas são, na realidade, números
    especie = int(especie)
    PCa = int(PCa)
    PCf = int(PCf)

    #criação de uma nova linha no banco de dados a cada vez que o for loop rodar
    bancoDados.append ([especie, PCa, PCf])

while True:
    #entrada da espécie e PCa, verificando se elas estão zeradas
    especie, PCa = input().split()
    especie = int (especie)
    PCa = int (PCa)

    if especie != 0 and PCa !=0:

        multiplicadorSoma = 0
        especieSoma = 0
    
        #cálculo da taxa média de evolução
        for sublist in bancoDados:
            if sublist[0] == especie:
                multiplicador = sublist[2]/sublist[1]
                multiplicadorSoma += multiplicador
                especieSoma += 1

        M = multiplicadorSoma/especieSoma

        #cálculo do PC da espécie após evoluir
        valorEvoluido = PCa * M

        #arredondamento para cima de um número decimal
        valorEvoluido = math.ceil(valorEvoluido)
        
        #saída do PC após evolução
        print (valorEvoluido)

    #caso PCa E espécie forem 0, o loop finaliza
    else:
        break
