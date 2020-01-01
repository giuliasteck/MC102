"""
Nome: Giulia Steck
RA: 173458
Entrada: Um valor inteiro em centavos, que deverá rodar num 
programa que calculará quais notas devem ser utilizadas para
cobrir esse valor.
Saída: quantidade de cada uma das notas utilizadas.
"""

#Entrada: um valor inteiro
valor = int(input())

#O valor1_x, sendo x correspondente a nota ou moeda a ser calculada,
#vai conter a quantidade de notas que podem ser utilizadas. Já o
#valor2_x indicará o quanto sobrou do valor inicial após a nota x já
#ter sido contabilizada. Dessa forma, o valor2_x passa a ser o novo
#valor a ser calculado para a próxima nota/moeda x, de valor inferior.

valor1_100 = valor//10000
valor2_100 = (valor%10000)

print (valor1_100, "nota(s) de R$ 100,00.")

valor1_50 = (valor2_100//5000)
valor2_50 = valor2_100%5000

print (valor1_50, "nota(s) de R$ 50,00.")

valor1_20 = valor2_50//2000
valor2_20 = valor2_50%2000

print (valor1_20, "nota(s) de R$ 20,00.")

valor1_10 = valor2_20//1000
valor2_10 = valor2_20%1000

print (valor1_10, "nota(s) de R$ 10,00.")

valor1_5 = valor2_10//500
valor2_5 = valor2_10%500

print (valor1_5, "nota(s) de R$ 5,00.")

valor1_2 = valor2_5//200
valor2_2 = valor2_5%200

print (valor1_2, "nota(s) de R$ 2,00.")

valor1_1 = valor2_2//100
valor2_1 = valor2_2%100

print (valor1_1, "moeda(s) de R$ 1,00.")

valor1_50cent= valor2_1//50
valor2_50cent = valor2_1%50

print (valor1_50cent, "moeda(s) de R$ 0,50.")

valor1_25cent = valor2_50cent//25
valor2_25cent = valor2_50cent%25

print (valor1_25cent, "moeda(s) de R$ 0,25.")

valor1_10cent = valor2_25cent//10
valor2_10cent = valor2_25cent%10

print(valor1_10cent, "moeda(s) de R$ 0,10.")

valor1_5cent = valor2_10cent//5
valor1_5cent = int(valor1_5cent)

print (valor1_5cent, "moeda(s) de R$ 0,05.")
