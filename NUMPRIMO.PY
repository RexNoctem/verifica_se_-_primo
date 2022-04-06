print("Programa que identifica se um número é primo\n")

numero = int(input("Verificar numeros primos ate: "))
mult=0

for divisores in range(2,numero):
    if (numero % divisores == 0):
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Não é primo")



