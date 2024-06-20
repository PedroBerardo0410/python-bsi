vet = [0]*30
i = 0

for i in range (0,30,1):
    vet[i] = input(f"Informe a posicao {i}:")


print(f"Os numeros na posicao impar e: ")

for i in range(0,30,1):
    if (i % 2 != 0):
        print(f"[{vet[i]}]", end =' ' )
        
# ou se tirar o if e colocar o for para ir de 2 em 2 da certo tmb
