numero = int(input("Digite o valor de n: "))
fatorial = 1
iteracao = 1

while iteracao <= numero:
    fatorial *= iteracao
    iteracao += 1

print(fatorial)