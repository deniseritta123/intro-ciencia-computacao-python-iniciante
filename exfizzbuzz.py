numero = int(input("Digite um número inteiro: "))

if numero % 5 == 0:
    print("FizzBuzz")
else:
    if numero % 3 == 0:
        print("FizzBuzz")
    else:
        print(numero)
