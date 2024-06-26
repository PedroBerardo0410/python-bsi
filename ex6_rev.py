'''
Faça um algoritmo que solicite N números inteiros
até que o número 0(zero) seja digitado.
Ao final o algoritmo deve informar o maior e
o menor número digitado.
OBS: O número 0(zero) não pode ser contado.
'''

num = 0
maior = 0
menor = 0

num = int(input("Informe o número: "))
maior = num
menor = num

while(num != 0):
    if(num > maior):
        maior = num
    if(num<menor):
        menor = num
    
    num = int(input("Informe o número: "))

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")

