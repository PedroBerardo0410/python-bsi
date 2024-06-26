'''
Uma escola está realizando matrículas para um curso aberto à comunidade,
com limite de 20 vagas. Assumindo que os alunos são cadastrados por computador,
escreva um algoritmo que:
Leia a idade e o sexo do aluno;
Informe que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;
Mostre a idade média dos candidatos;
Mostre a quantidade de mulheres inscritas;
Mostre os candidatos (homens e mulheres) maiores de idade.

'''

idade = 0
sexo = ""
media = 0.0
qntd_mulheres = 0
maiores_idade = 0
soma = 0

for i in range(1,21,1):
    idade = int(input("Informe a idade do aluno:"))
    sexo = input("Informe o sexo do aluno:")
    
    if(sexo.upper() == "F"):
        qntd_mulheres += 1
    if(idade>= 18):
        maiores_idade += 1
    soma += idade

print("A turma está lotada")
media = soma / 20

print(f"A idade média dos inscritos é de {media:,.2f}: ")
print(f"A quantidade de mulheres inscritas é de {qntd_mulheres}: ")
print(f"A quantidade de inscritos maiores de idade é de {maiores_idade}: ")

