print("Programa que identifica se um número é primo\n")

numero = int(input("Verificar numeros primos ate: "))
qtd_divisores=0

for divisores in range(2,numero):
    if (numero % divisores == 0):
        qtd_divisores += 1

if(qtd_divisores==0):
    print("É primo")
else:
    print("Não é primo")



