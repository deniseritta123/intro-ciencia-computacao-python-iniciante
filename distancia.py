import math

coordenadaX1 = int(input("Digite a primeira coordenada x: "))
coordenadaY1 = int(input("Digite a primeira coordenada y: "))
coordenadaX2 = int(input("Digite a segunda coordenada x: "))
coordenadaY2 = int(input("Digite a segunda coordenada y: "))

if (math.sqrt((coordenadaX1 - coordenadaX2) ** 2 + (coordenadaY1 - coordenadaY2) ** 2)) >= 10:
    print("longe")
else:
    print("perto")