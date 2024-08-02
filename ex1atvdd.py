'''
Faça um algoritmo que receba 5 números e ao final mostre quem é o maior e o menor número digitado.
Deve-se fazer uma função para verificar o maior e outra para verificar o menor.
O menor e o maior número devem ser retornados para o programa principal para, então, serem mostrados.
'''
#
def maior(numeros):
    maior_num = numeros[0]
    for num in numeros:
        if num > maior_num:
            maior_num = num
    return maior_num


def menor(numeros):
    menor_num = numeros[0]
    for num in numeros:
        if num < menor_num:
            menor_num = num
    return menor_num

      

numeros = [0] * 5
for i in range(5):
    numeros[i] = float(input(f"Digite o número {i+1}: "))
    
maior_numero = maior(numeros)
menor_numero = menor(numeros)
    
print(f"O maior número digitado é: {maior_numero}")
print(f"O menor número digitado é: {menor_numero}")

    
    