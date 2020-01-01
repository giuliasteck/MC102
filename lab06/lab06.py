NumeroTimes = int(input())
#número de partidas de cada time
NumeroJogos = (NumeroTimes*2)-2
#número do total de partidas
Partidas = (NumeroJogos*NumeroTimes)/2
Partidas = int(Partidas)

dicionario = {} #golspro
Times = []
timesTodos = []
GC = {} #gols contra
V = {} #vitorias
D = {} #derrotas
E = {} #empates

for i in range (Partidas):
    linhaEntrada = input()
    dadosPartida = linhaEntrada.split()
    timesTodos.append(dadosPartida[0])

    #saldo de gols
    if dadosPartida[0]in dicionario:
        dicionario[dadosPartida[0]] = dicionario[dadosPartida[0]]+ float(dadosPartida[1])
    if not(dadosPartida[0] in dicionario):
        dicionario[dadosPartida[0]]= float(dadosPartida[1])
    if dadosPartida[3 ]in dicionario:
        dicionario[dadosPartida[3]] = dicionario[dadosPartida[3]]+ float(dadosPartida[4])
    if not(dadosPartida[3] in dicionario):
        dicionario[dadosPartida[3]]= float(dadosPartida[4])

    #número de gols contra
    if dadosPartida[0]in GC:
        GC[dadosPartida[0]] = GC[dadosPartida[0]]+ float(dadosPartida[4])
    if not(dadosPartida[0] in GC):
        GC[dadosPartida[0]]= float(dadosPartida[4])
    if dadosPartida[3]in GC:
        GC[dadosPartida[3]] = GC[dadosPartida[3]]+ float(dadosPartida[1])
    if not(dadosPartida[3] in GC):
        GC[dadosPartida[3]]= float(dadosPartida[1])
    
    #numero de vitorias
    if dadosPartida[1] > dadosPartida[4]:
        if dadosPartida[0] in V:
            V[dadosPartida[0]] += 1
        if not dadosPartida[0] in V:
            V[dadosPartida[0]] = 1

    if dadosPartida[4] > dadosPartida[1]:
        if dadosPartida[3] in V:
            V[dadosPartida[3]] += 1
        if not dadosPartida[3] in V:
            V[dadosPartida[3]] = 1

    #numero de derrotas
    if dadosPartida[4] > dadosPartida[1]:
        if dadosPartida[0] in D:
            D[dadosPartida[0]] += 1
        if not dadosPartida[0] in D:
            D[dadosPartida[0]] = 1

    if dadosPartida[1] > dadosPartida[4]:
        if dadosPartida[3] in D:
            D[dadosPartida[3]] += 1
        if not dadosPartida[3] in D:
            D[dadosPartida[3]] = 1
    
    #numero de empates
    if dadosPartida[4] == dadosPartida[1]:
        if dadosPartida[0] in E:
            E[dadosPartida[0]] += 1
        if not dadosPartida[0] in E:
            E[dadosPartida[0]] = 1

        if dadosPartida[3] in E:
            E[dadosPartida[3]] += 1
        if not dadosPartida[3] in E:
            E[dadosPartida[3]] = 1

#lista com o nome dos times
for i in timesTodos:
    if i not in Times:
        Times.append(i)



print(dicionario)
print(GC)
print(V)
print(D)
print(E)
for i in Times:
    SD = dicionario[i] - GC[i]
    NGT = dicionario[i]
    NV = V[i]
    Pontuação = V[i]*3+D[i]*0 + E[i]*1
    print(SD, NGT, NV, Pontuação)

    
