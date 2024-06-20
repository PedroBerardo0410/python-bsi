i=0
sexo=""
idade=0
soma_idade=0
media_idade=0
masculino=0
feminino=0
velha = 0
velho = 0
for i in range(0,5,1):
    idade = int(input("Informe a idade: "))
    soma_idade += idade
    sexo = input("Informe seu sexo, M - masculino, F - feminino: ").upper()
    if(sexo == 'F'):
        feminino += 1
    
    if(sexo == 'M') and (idade >= 18):
       velho += 1 


    if (sexo == 'F') and ( idade >= 18):
        velha += 1 

    
        

media_idade = soma_idade / 5


print(f"A turma está lotada")
print(f"O candidato {i+1} é maior de idade")
print(f"A média das idades é {media_idade}")
print(f"A quantidade de mulheres escrita é de {feminino}")
print(f"A quantidade de homens maiores de 18 anos é de: {velho}")
print(f"A quantidade de mulheres maiores de 18 anos é de: {velha}")




