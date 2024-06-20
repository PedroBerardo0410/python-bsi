n1 = 0
n2 = 0
resultado = 0

def somar_numeros (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

print(f"A soma dos numeros e: {somar_numeros(n1,n2)}")