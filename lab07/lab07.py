#notas das provas conceituais
notasAc = [float(x) for x in input().split()]

#entrada das tuplas
def tupla_float_int(x):
    x=x[1:-1]
    x = x.split(',')
    f = float(x[0])
    i = int(x[1])
    return(f,i)

notasLab = [tupla_float_int(x) for x in input().split()]

#entrada da nota das provas
notasProvas = input().split()
for i in notasProvas:
    i = float(i)

#frequência do aluno
freq = int(input())

#média das atividades conceituais
quantidade = 0
for i in range(len(notasAc)):
    quantidade += 1
somaAtividade = sum(notasAc)
mediaAtividades = somaAtividade/quantidade

#média das Provas
notasProvas[0] = float(notasProvas[0])*2
notasProvas[1] = float(notasProvas[1])*3
mediaProvas = (notasProvas[0]+notasProvas[1])/5

somaNotas = 0
somaPesos = 0
#média dos Labs
for i in range(len(notasLab)):
    notasLab[i] = list(notasLab[i])
for i in range(len(notasLab)):
    notasLab[i][0] = notasLab[i][0]*notasLab[i][1]
    somaNotas += notasLab[i][0]
    somaPesos += notasLab[i][1]
mediaLabs = somaNotas/somaPesos

print('Media das atividades conceituais:', format(mediaAtividades,".1f"))
print('Media das tarefas de laboratorio:', format(mediaLabs,".1f"))
print('Media das provas:',format(mediaProvas,".1f"))

if freq >= 75:
    
    if mediaLabs >= 5 and mediaProvas >= 5:
        mediaFinal = (6*mediaProvas + 3*mediaLabs + 1*mediaAtividades)/10
        if mediaFinal >= 5:    
            print('Aprovado(a) por nota e frequencia.')
        else:
            Exame = float(input())
            mediaFinal = (mediaFinal+Exame)/2
            if mediaFinal < 5:
                print('Reprovado(a) por nota.')
            if mediaFinal >= 5:
                print('Aprovado(a) por nota e frequencia.')
           
    elif mediaLabs < 2.5 or mediaProvas < 2.5:
        mediaFinal = min(mediaLabs,mediaProvas)
        print('Reprovado(a) por nota.')
    
    else:
        Exame = float(input())
        print('Nota no exame:',Exame)
        mediaFinal = (min(mediaLabs,mediaProvas)+Exame)/2
        if mediaFinal < 5:
            print('Reprovado(a) por nota.')
        if mediaFinal >= 5:
            print('Aprovado(a) por nota e frequencia.')

if freq < 75:
    mediaFinal = min(mediaLabs,mediaProvas)
    print('Reprovado(a) por frequencia.')

print('Media final:',format(mediaFinal, ".1f"))

