import math

catOposto = float(input('Digite o cateto oposto: '))
catAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdjacente)
print('Valor da hipotenusa: {:.2f}'.format(hipotenusa))
