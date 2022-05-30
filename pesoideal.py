#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que #calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


genero = str(input("digite o sexo da pessoa que será calculado o peso ideal: \n (caso homem digite 'h' caso for uma mulher digite 'm') ")).upper()

h = float(input("digite a sua altura(em cm): "))

if genero == ('H'):
    pesoideal = ( (72.7*(h/100)) - 58)
    print ('seu peso ideal é:', pesoideal)

elif genero == ('M'):
    pesoideal = (62.1* (h/100) - 44.7)
    print ('seu peso ideal é:', pesoideal)
else:
    print("reinicie a aplicação algo deu errado")