vetor = []
PAR = []
IMPAR = []

for numero in range(0, 20):
    vetor.append(int(input("Digite um numero inteiro: ")))

for numero in range(0, 20):
    if vetor[numero] % 2 == 0:
        PAR.append(vetor[numero])
    else:
        IMPAR.append(vetor[numero])

print("Vetor com 20 elementos: " + str(vetor))
print("Vetor com elementos pares: " + str(PAR))
print("Vetor com elementos impares: " + str(IMPAR))