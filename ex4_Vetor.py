vet = [0.0]*5
vet1 = [0.0]*5

for i in range (0,5,1):
    vet[i] = float(input(f"Informe o {i}° valor do vetor: "))

print(f"O vetor original e: ")

for i in range (0,5,1):
    print(f"[{vet[i]}]", end = ' ')    

for i in range (0,5,1):
    if( i % 2 == 0):
        vet1[i] = vet[i] * 1.02
    else:
        vet1[i] = vet[i] * 1.05
print()
print(f"O vetor resultante e: ")

for i in range(0,5,1):
    print(f"[{vet1[i]}]", end = ' ')



