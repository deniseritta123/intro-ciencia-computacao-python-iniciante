def vogal(letra):
    vogais = "aeiouAEIOU"
    i = 0
    while i < len(vogais):
        if letra == vogais[i]:
            return True
        i += 1
    return False