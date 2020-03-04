#Giulia Steck
#Descricao: esse código tem como entrada números negativos
#ou positivos, que representam, respectivamente, ataque recebido
#e ataque dado por Ryu. Se o valor inserido for um numero perfeito,
#ele sera multiplicado por 3. Se for triangular, multiplicado por 2.
#Se for perfeito e triangular, multiplicado por 3.
#Como saidas, o programa mostra a vida de Ryu, de Ken e quem venceu.


import math

#Essa função verifica se o a variável valor inserida
#é um número triangular e/ou perfeito e a multiplica
def transformaNumero(n):
    valorAbs = abs(n)
    
    #Verificar se é número triangular
    Triangular = (math.sqrt(8*valorAbs+1)- 1)/2
    soma = 0

    #Verificar se é número perfeito
    for i in range (1,valorAbs):
        if (valorAbs%i == 0):
            soma += i

    if soma == valorAbs: #condição número perfeito
        n *= 3 
    elif Triangular == int(Triangular): #condição número perfeito
        n *= 2
    
    return n

Ryu = 0
Ken = 0

#loop que roda dois rounds e define um vencedor no fim
for i in range (0,2):
    pvRyu = 2000
    pvKen = 2000
    valor = transformaNumero(int(input()))
    totalDano = 0

    #Loop que verifica se valor é negativo e, caso seja,
    #esse valor é verificado pela função transformaNumero
    #e Ryu tem esse valor descontado de sua vida
    while pvRyu > 0 and pvKen > 0:
        if valor < 0:
            totalDano = -valor
            while valor < 0 and pvRyu-totalDano > 0:
                valor = transformaNumero(int(input()))
                if valor < 0:
                    totalDano -= valor
            print("Ryu: {:d} - {:d} = {}".format(pvRyu, totalDano, pvRyu-totalDano))

            pvRyu -= totalDano
            totalDano = 0 #Garantir que a variável totalDano desse loop seja diferente
                          #da varíavel totalDano do loop seguinte

        #Caso o valor inserido seja positivo, esse loop passa a ser rodado
        #e continua rodando até que uma varíavel negativa seja inserida ou
        #a vida de algum dos lutadores seja zerado
        if valor > 0 and pvRyu > 0:
            totalDano = valor
            while valor > 0 and pvKen-totalDano > 0: 
                valor = transformaNumero(int(input())) #função que verifica, dentro do loop
                                                       #se valor é numero perfeito e/ou triangular
                if valor > 0:
                    totalDano += valor
            print("Ken: {:d} - {:d} = {}".format(pvKen, totalDano, pvKen-totalDano))

            pvKen -= totalDano
            totalDano = 0

    #atribui pontos para o lutador vencedor de cada round
    if pvRyu > pvKen:
        Ryu = Ryu + 1
    else:
        Ken = Ken + 1

#verifica os pontos atribuidos anteriormente e
#printa o vencedor de acordo com quem tem mais pontos
if Ryu > Ken:
    print("Ryu venceu")
elif Ryu < Ken:
    print("Ken venceu")
elif Ryu == Ken:
    print("empatou")
