vet = [0]*10


for i in range(0,10,1):
    vet[i] = input(f"Digite o { i+1 }° numero do vetor: ")

print(f"Os numeros na ordem inversao sao: ")

for i in range(9,-1,-1):
    print(f"[{vet[i]}]", end='  ')

