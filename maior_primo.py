n = int(input("defina o número a analisar: "))

def maior_primo(n):
    numero = n
    while numero > 1:
        if eh_primo(numero):
            return numero
        numero -= 1

def eh_primo(numero):
    if numero == 2:
        return True
    if numero < 2 or numero % 2 == 0:
        return False
    i = 3
    while i <= int(numero ** 0.5):
        if numero % i == 0:
            return False
        i += 2
    return True


print(maior_primo(n))