'''
Faça um algoritmo que receba um vetor A de dez elementos inteiros, por parâmetro. Ao final dessa função, o vetor B deve conter os valores seguindo a regra: 
se o valor de A na mesma posição de B for par o mesmo deve ser multiplicado por 5 caso, se for ímpar deve ser somado com 3.
 Esses testes devem ser feitos em uma função.
'''
def processa_vetor(A):
    B = [0] * len(A)  # Inicializa o vetor B com o mesmo tamanho de A
    for i in range(len(A)):
        if A[i] % 2 == 0:  # Verifica se o número é par
            B[i] = A[i] * 5
        else:  # O número é ímpar
            B[i] = A[i] + 3
    return B


A = [0] * 10  # Inicializa o vetor A com 10 elementos
for i in range(10):
    A[i] = int(input(f"Digite o {i+1}º número inteiro para o vetor A: "))
    
B = processa_vetor(A)
    
print("Vetor A:", A)
print("Vetor B:", B)