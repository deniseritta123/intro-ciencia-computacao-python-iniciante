def maior_primo(n):
    k = n        
    while k > 1 and primo(k)==False:
        k = k - 1
    return k
def primo(k):
    aux = True    
    div = 2
    while k > div:     
        if k % div == 0:
            aux = False
        div = div + 1
    return aux