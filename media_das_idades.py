i=0
soma = 0
idadema = 0
idademe = 0
qntd = 0
media_idade = 0

qntd = int(input("Informe a quantidade de pessoas: "))

for i in range(0,qntd,1):
    idades = int(input("Informe as idades: "))
    if (i==0):
        idadema = idades
        idademe = idades
    else: 
        if(idades > idadema):
            idadema = idades
        if(idades < idademe):
            idademe = idades
    soma += idades
media_idade = soma / qntd
print(f"A média das idades é {media_idade}")
print(f"A menor idade é: {idademe}")
print(f"A maior idade é: {idadema}")