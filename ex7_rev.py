'''
Foi feita uma pesquisa de audiência de canal de TV
em várias casas de uma certa cidade, num determinado dia.
    Para cada casa visitada, é fornecido o número do
canal (9, 12, 23 ou 40).
    Fazer um algoritmo que:
       - leia um número indeterminado de dados,
         até que seja digitado o canal 0(zero);
       - Calcule e mostre a porcentagem de
         audiência de cada emissora;
       - Caso seja digitado algum canal fora dos
         apresentado acima, informar como outros canais;
       - O número 0(zero) não pode ser considerado um canal.

'''

q9 = 0
p9 = 0.0
q12 = 0
p12 = 0.0
q23 = 0
p23 =0.0
q40 = 0
p40 =0.0
qoutros= 0 
poutros=0.0
i =0
num = 1

while(num!=0):
    num = int(input("Informar o canal 9, 12, 23 ou 40: "))
    if (num == 9):
        q9 += 1
        i+=1
    elif (num == 12):
        q12 +=1
        i+=1
    elif( num == 23):
        q23 += 1
        i+=1
    elif(num == 40):
        q40 +=1
        i+=1
    elif(num!=0): 
        qoutros +=1
        i+=1
if (i!=0):
    p9 = (q9*100)/i
    p12 = (q12*100)/i
    p23 = (q23*100)/i
    p40 = (q40*100)/i
    poutros = (qoutros*100)/i

    
print(f"CANAL 9: {p9:,.2f}%")
print(f"CANAL 12: {p12:,.2f}%")
print(f"CANAL 23: {p23:,.2f}%")
print(f"CANAL 40: {p40:,.2f}%")
print(f"OUTROS CANAIS: {poutros:,.2f}%")


