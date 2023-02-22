n = int(input("Digite um número inteiro: "))

divisor = 2
primo = True

while divisor < n and primo:
    if n % divisor == 0:
        primo = False
    divisor += 1

if primo:
    print("primo")
else:
    print("não primo")