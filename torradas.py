num_torradas = int(input("digite quantas torradas vai comer: "))
calorias_torrada = 200


def linear_function(calorias_torrada, num_torradas):
    y = (num_torradas * calorias_torrada )
    return y


y = linear_function(calorias_torrada, num_torradas)
print("você vai ingerir", y, "calorias")