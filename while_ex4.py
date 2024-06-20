canal = 1
nove = 0
doze = 0
vinte_tres = 0
quarenta = 0
dif = 0
total = 0
pnove = 0
pdoze = 0
pvinte_tres = 0
pquarenta = 0
outros = 0


while canal != 0:
    canal = int(input("Informe o número do canal - 9 - 12 - 23 - 40:"))
    if(canal == 9):
        nove+= 1
    elif(canal == 12):
        doze+= 1
    elif(canal == 23):
        vinte_tres+= 1
    elif(canal == 40):
        quarenta+= 1
    elif(canal !=0 and canal != 9 and canal != 12 and canal != 23 and canal != 40):
        dif += 1

total = (nove + doze + vinte_tres + quarenta + dif)
pnove = (nove/total)*100
pdoze = (doze/total)*100
pvinte_tres = (vinte_tres/total)*100
pquarenta = (quarenta/total)*100
outros = (dif/total)*100




print(f"A porcentagem do canal 9 é de: {pnove:.2f}%")
print(f"A porcentagem do canal 12 é de: {pdoze:.2f}%")
print(f"A porcentagem do canal 23 é de: {pvinte_tres:.2f}%")
print(f"A porcentagem do canal 40 é de: {pquarenta:.2f}%")
print(f"A porcentagem de outros canais é de: {outros:.2f}%")


    