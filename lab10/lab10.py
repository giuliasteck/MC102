#Giulia Steck 173458
#Descricao: o objetivo do programa e simular uma luta entre Ryu e Ken
#O programa aceita como entrada valores inteiros, sendo que os negativos representam que Ryu foi atacado e os positivos indicam que Ken foi atacado. Como saida, temos os valores das vidas apÃ³s os ataques serem efetuadose quem foi o vencedor (quem ganhou mais rounds)

#definiÃ§Ã£o das variÃ¡veis fora do loop
Ryu = 0
Ken = 0

for i in range (0,2): #fazer o loop rodar duas vezes (2 rounds)
    pvRyu = 50 #vida inicial dos lutadores
    pvKen = 50
    valor = int(input()) #inserir um valor inicial que entrarÃ¡ nos loops

    while pvRyu > 0 and pvKen > 0: #condiÃ§Ã£o em que nenhum lutador perdeu
        if valor < 0: #momento em que Ryu sofre um ataque
            totalDano = -valor #totalDano Ã© a variavel utilizada para somar os valores negativos que entram seguidamente
            while valor < 0 and pvRyu-totalDano > 0: #esse loop garante que todos os nÃºmeros negativos se somem antes de mostrar uma saÃ­da
                valor = int(input()) 
                if valor < 0: 
                    totalDano -= valor
            print("Ryu: {:d} - {:d} = {}".format(pvRyu, totalDano, pvRyu-totalDano)) #saÃ­da que mostra os danos sofridos por Ryu

            pvRyu -= totalDano

        if valor > 0 and pvRyu > 0: 
            totalDano = valor #totalDano, nesse caso, soma os valores positivos que entram seguidamente
            while valor > 0 and pvKen-totalDano > 0: #soma dos nÃºmeros positivos antes do programar printar uma saida
                valor = int(input())
                if valor > 0:
                    totalDano += valor #soma dos numeros positivos desse loop

            print("Ken: {:d} - {:d} = {}".format(pvKen, totalDano, pvKen-totalDano)) #saÃ­da que mostra os danos sofridos por Ken

            pvKen -= totalDano

#conta quantos rounds cada lutador ganhou
    if pvRyu > pvKen:
        Ryu = Ryu + 1
    else:
        Ken = Ken + 1

#saÃ­da que vai indicar quem venceu
if Ryu > Ken:
    print ("Ryu venceu")
elif Ryu < Ken:
    print ("Ken venceu")
elif Ryu == Ken:
    print ("empatou")


