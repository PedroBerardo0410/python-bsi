'''
Escrever um algoritmo que leia os dados de N pessoas
(nome, sexo(M/F), idade e saúde(B/R)) e informe
se está apta ou não para cumprir o serviço militar obrigatório.
Informe os totais de aptos e não aptos no final do algoritmo.
Se o candidato estiver apto deve ser mostrado o seu nome e a mensagem que está apto.
Para estar apto o candidato deve possuir 18 anos,
ser do sexo masculino e estar com a saúde boa.
Caso o candidato não possa servir deve ser mostrado o seu nome e o motivo.
O sistema deve ficar solitando dados até que seja digitado N.

'''
num = 0
nome = ""
sexo = ""
idade = 0
saude = ""
continuar = ""
t_aptos = 0
t_n_aptos = 0

continuar = "S"
while(continuar.upper() == "S"):
    nome = input("Informe o Nome: ")
    sexo = input("Informe o Sexo: ")
    idade = int(input("Informe a idade: "))
    saude = input("Informe a saúde B - boa, R - ruim: ")
    if (idade>=18):
        if(sexo.upper() == "M"):
            if(saude.upper() == "B"):
                print(f"O alistado {nome}, está apto para servir o exército.")
                t_aptos+=1
            else:
                print(f"O candidato {nome}, não está apto por conta de sua saúde ser ruim.")
                t_n_aptos +=1
        else:
            print(f"O candidato {nome}, não está apto por conta de seu sexo não ser do gênero masculino.")
            t_n_aptos+=1
    else:
        print(f"O candidato {nome}, não está apto por conta de não ser maior de idade.")
        t_n_aptos+=1
    continuar = input("Deseja continuar? S ou N")

print(f"O Total de Aptos é: {t_aptos}")
print(f"O Total de NÃO Aptos é: {t_n_aptos}")