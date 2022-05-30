#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;

a = float(input("digite o valor de um lado do triangulo: "))
b = float(input("digite o valor de outro lado do triangulo: "))
c = float(input("digite o valor de outro lado do triangulo: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("não é um triangulo")

elif (a == b) and (a == c):
    print('Equilatero')

elif (a == b) or (b == c) or (a == c):
    print("Isoceles")

else:
    print("Escaleno")