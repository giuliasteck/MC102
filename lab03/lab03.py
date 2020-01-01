objeto = input(str())

if objeto == 'Q' or objeto == 'L' or objeto == 'C':
    caractere = input(str())
    lado = int(input())
    if lado < 3:
        print('Dimensao incorreta.')
    else:
        #Quadrado
        if objeto == 'Q':
            for i in range(lado):
                for j in range(lado):
                    if i in [0,lado-1] or j in [0,lado-1]:
                        print (caractere, end='')
                    else:
                        print(' ', end='')
                print()

        #Losango
        elif objeto == 'L':
            print((lado-1)*" "+caractere)
            for i in range(lado-2,-1,-1):
                print(i*" "+caractere+(-2*i+2*lado-3)*" "+caractere)

            for i in range(1,lado-1):
                print(i*" "+caractere+(-2*i+2*lado-3)*" "+caractere)
            print((lado-1)*" "+caractere)

        #Cruz
        elif objeto == 'C':
            print(lado*" "+caractere*lado)
            for i in range(1,lado-1):
                print(lado*' '+caractere+(lado-2)*' '+caractere)
            print(caractere*lado*3)
            for i in range(1,lado-1):
                print(caractere+(lado-2)*' '+2*caractere+(lado-2)*' '+2*caractere+(lado-2)*' '+caractere)
            print(caractere*lado*3)
            for i in range(1,lado-1):
                print(lado*' '+caractere+(lado-2)*' '+caractere)
            print(lado*' '+caractere*lado)



elif objeto == 'R' or objeto == 'P':
    caractere = input(str())
    largura = int(input())
    altura = int(input())
    if altura<3 or largura<3:
        print('Dimensao incorreta.')
    else:
        #Retangulo
        if objeto == 'R':
            print(caractere*largura)
            for i in range(1, altura-1):
                print(caractere+(largura-2)*' '+caractere)
            print(caractere*largura)

        
        #Paralelogramo
        elif objeto == 'P':
            print(str(caractere)*largura)
            for i in range (1,altura-1):
                print(i*" "+ str(caractere)+(largura-2)*" "+str(caractere) )
            print((altura-1)*" "+largura*caractere)


else:
    print("Objeto incorreto.")

