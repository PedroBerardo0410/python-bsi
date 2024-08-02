'''
Faça um algoritmo que crie um vetor real de 20 posições: as 10 primeiras são informadas pelo usuário e as 10 seguintes serão colocadas de forma automática pelo algoritmo sendoos mesmos números porém em ordem inversa.
Ex: Digitando os número das 10 primeira posições
1  2  3  4  5  6  7  8  9  10
O vetor final deve ser
1  2  3  4  5  6  7  8  9  10  10 9  8  7  6  5  4  3  2  1

'''

vet = [0] * 20


for i in range(10):
    vet[i] = int(input(f"Digite o número para a posição {i+1}: "))

for i in range(10):
    vet[10 + i] = vet[9 - i]


print("O vetor final é:", end='  ')
print(vet)

