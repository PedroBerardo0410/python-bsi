matriz = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]

for i in range(0,5,1):
    for j in range(0,5,1):
        matriz[i][j] = int(input(f"Informe o numero da linha [{i+1}] e coluna [{j+1}]: "))
       
print(f"A matriz normal fica: ")

for i in range (0,5,1):
    for j in range(0,5,1):
         print([matriz[i][j]], end = ' ' )
    print()

print(f"A diagonal principal fica: ")

for i in range (0,5,1):
    for j in range(0,5,1):
        if (i==j):
            print(f"[{matriz[i][j]}]", end = ' ')
        else:
            print(" ", end = ' ')
    print()

