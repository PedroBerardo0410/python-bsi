'''
Construir um algoritmo que solicite um número e calcule a tabuada deste número
'''

num = 0

num = int(input("Informe um número para ser feito a tabuada: "))

for i in range(1,11,1):
    print(f"{num} X {i} = {num*i}")


