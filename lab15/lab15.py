"""
Nome: Giulia Steck
RA: 173458
Descrição: o programa é uma espécie de editor de textos que pode]
deletar, substituir ou inverter as palavras presentes na string de
entrada (discurso). Ademais, ele apresenta como saída a frase 
resultante dessas ações ao fim da realização de cada ação.
"""
import re

pontuacao = [".", ",", "?", "!", ":"]

#função que checa se o elemento é uma pontuação
#ou não
def listToString(lista):
    saida = ""
    for i, e in enumerate(lista):
        if i == 0:
            saida += e
        #se e não for uma pontuação, é printado um
        #espaço e o elemento
        elif e not in pontuacao:
            saida += " " + e
        #se for pontuação, ela é printada em espaço
        else:
            saida += e

    return saida

discurso = input()
print(discurso)
#separar a string discurso em uma lista, separada por espaços
#e pontuações
discurso = re.findall (r"[\w']+|[.,?!:]", discurso)

while True:
    acaoEdicao = input()

    #caso em que a palavra escrita será deletada
    if acaoEdicao == "D":
        palavra_deletar = input ()
        #ativar case Insensivity: tanto a lista como o
        #input da palavra a ser deletada ficam em letras
        #minúsculas para serem comparados
        deletarLower = (palavra_deletar.lower())
        tmpDiscurso = []
        #criação de variável para, caso haja uma pontuação,
        #e/ou a palavra deletada, estas serão "puladas" e 
        #não serão printadas
        flag = False
        for elem in discurso:
            if elem.lower() == deletarLower:
                flag = True
            elif flag and elem in pontuacao:
                flag = False
            else:
                tmpDiscurso.append(elem)
                flag = False
        discurso = tmpDiscurso[:]
        #printa utilizando a função do ínicio (sem espaço entre palavra
        #anterior e pontuação, com espaço entre duas palavras, com espaço
        #entre pontuação e palavra seguinte e sem espaço após elemento final)
        print(listToString(discurso))

    #caso em que palavra_velha é subtituida por palavra_nova
    if acaoEdicao == "R":
        palavra_velha = input()
        velhaLower = (palavra_velha.lower())
        palavra_nova = input()
        discurso = [i if i.lower() != velhaLower else palavra_nova for i in discurso]
        print(listToString(discurso))

    #caso em que a palavra é invertida
    if acaoEdicao == "I":
        palavra_inverter = input()
        inverterLower = (palavra_inverter.lower())
        discurso = [i if i.lower() != inverterLower else i[::-1] for i in discurso]
        print (listToString(discurso))

    #caso em que o programa para de rodar
    if acaoEdicao == "Q":
        break

