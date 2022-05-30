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