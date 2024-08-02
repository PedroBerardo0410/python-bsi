'''
Faça um algoritmo que leia o nome e a média final de 5 alunos e guarde em um vetor.
Ao final deve ser mostrado o nome do aluno com maior média.

'''
nomes = [" "] * 5
medias = [0.0] * 5
mm = medias[0]
alunomm = nomes[0]


for i in range(5):
    nomes[i] = input(f"Digite o nome do {i+1}° aluno: ")
    medias[i] = float(input(f"Digite a média final do {i+1}° aluno: "))
    
for i in range(5):
    if medias[i] > mm:
        mm = medias[i]
        alunomm = nomes[i]

print(f"O aluno com a maior média é: {alunomm} com a média de {mm}.")



