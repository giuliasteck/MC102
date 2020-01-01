"""
Nome: Giulia Steck
RA: 173458
"""
Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())

MariaFerias = input()
MarcosFerias = input()

Maria13 = int(input())
Marcos13 = int(input())

valorHotel = float(input())
valorPassagem = float(input())
Custo = valorHotel + valorPassagem

Carla = 0
Ferias = 0
Salario = 0

#checar se notas da Carla são suficientes
if Nota1 >= 7 and Nota2 >= 7 and Nota3 >= 7:
    Carla = 1
else:
    print ("NAO. As notas da Carla nao foram suficientes.")

#checar se ambos estão de férias
if Carla == 1:
    if MariaFerias == 'Sim' and MarcosFerias ==  'Sim':
        Ferias = 1
    else:
        print ("NAO. O casal nao esta de ferias.")

#checar se alfum deles recebeu 13o antes do dia 11
if Ferias == 1:
    if Maria13 < 11 or Marcos13 < 11:
        Salario = 1
    else:
        print ("NAO. Nenhum 13o salario foi liberado a tempo.")

#checar se custo da viagem é menor de 10.000
if Salario == 1:
    if Custo <= 10000:
        print("SIM!!!")
    else:
        print("NAO. O valor total e muito alto.")

