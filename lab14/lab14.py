"""
Nome: Giulia Steck
RA: 173458
Descrição: esse programa tem como objetivo checar a ação de 4 empresas
a partir da entrada d dias (cada empresa tem um valor de sua ação em cada
um dos dias) e checar qual a combinação de compra/venda de ações gerará o 
lucro máximo. Como saída temos as empresas das quais se comprou a ação,
em que dia ela foi comprada, que dia ela foi vendida e o lucro gerado a 
partir disso. Por fim, tem-se o cálculo do lucro total.
"""

#número de dias em que o programa rodará
d = int(input())

#definição das listas que serão montadas para definir o valor
#de cada empresa em cada um dos d dias
bloco1 = []
bloco2 = []
bloco3 = []
bloco4 = []

#inserção dos valores de cada empresa em cada um dos d dias
for i in range(d):
    #a função .append insere cada valor, de cada loop na lista
    #correspondente à empresa
    empresa1 = float(input())
    bloco1.append (empresa1)

for i in range(d):
    empresa2 = float(input())
    bloco2.append (empresa2)

for i in range(d):
    empresa3 = float(input())
    bloco3.append (empresa3)

for i in range(d):
    empresa4 = float(input())
    bloco4.append (empresa4)

#criação de uma lista vazia que receberá os valores de cada uma
#das gerações possíves decorrentes dos loops abaixo
maxEmpresa = []

#loops que veem os dias de compra e venda possíveis para cada uma
#das quatro empresas
for c1 in range(d):
    for v1 in range(c1+1, d):
        for c2 in range(d):
            for v2 in range(c2+1, d):
                for c3 in range(d):
                    for v3 in range(c3+1, d):
                        for c4 in range(d):
                            for v4 in range(c4+1, d):
                                #definição de lucro (dia da
                                #venda - dia da compra)
                                lucro4 = bloco4[v4]-bloco4[c4]
                                lucro3 = bloco3[v3]-bloco3[c3]
                                lucro2 = bloco2[v2]-bloco2[c2]
                                lucro1 = bloco1[v1]-bloco1[c1]
                                
                                #lista que guarda os dias de compra, venda e seus respectivos lucros
                                dias = [(c1,v1, lucro1), (c2,v2, lucro2), (c3,v3, lucro3), (c4,v4, lucro4)]
                                #checa presença de disjunções entre os dias de compra e venda
                                for i, a in enumerate(dias):
                                    for j, b in enumerate(dias):
                                        if j == i:
                                            continue
                                        #se início de a menor ou igual a ínicio de b e fim de a maior que inicio
                                        #de b ou vice e versa = há disjunção entre os dias de compra e venda
                                        elif (a[0] <= b[0] and a[1] > b[0]) or (b[0] <= a[0] and b[1] > a[0]):
                                            #entretando, caso haja disjunção, a sublista de menor lucro será zerada
                                            if a[2] > b[2]:
                                                dias[j] = (0,0,0)
                                            else:
                                                dias[i] = (0,0,0)
                                        
                                lucro = sum(x[2] for x in dias)
                                dias.append(lucro)
                                maxEmpresa.append(dias)


resposta = max(maxEmpresa, key=lambda x: x[4])

for i, e in enumerate(resposta[:-1]):
    #as sublistas zeradas não terão seu resultado impresso (nenhuma ação foi efetuada)
    if e != (0,0,0):
        print("acao %d: compra %d, venda %d, lucro %.2f" % (i+1, e[0]+1, e[1]+1, e[2]))
print("Lucro: %.2f" % (resposta[-1]))
