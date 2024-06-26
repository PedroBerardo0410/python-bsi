'''
Construir um algoritmo que leia a idade de N pessoas.
O sistema deve calcular: a média das idades, a menor e a maior idade informada

'''
n = 0
idade = 0
media = 0.0
me = 0
ma = 0
soma = 0

n = int(input("Informe quantas idades serão digitas: "))

for i in range (0,n,1):
    idade = int(input("Informe a idade: "))
    if (idade > ma):
            ma = idade
    if ( idade < me):
            me = idade
    soma += idade
    media = soma / n

print(f"A média das idades é de: {media:,.2f}")
print(f"A maior idade é de: {ma}")
print(f"A menor idade é de: {me}")

