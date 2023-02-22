num = int(input("Digite um número inteiro: "))

digito_anterior = num % 10  
num //= 10 

while num > 0:
    digito_atual = num % 10
    if digito_atual == digito_anterior:
        print("sim")
        break
    digito_anterior = digito_atual
    num //= 10
else:  
    print("não")