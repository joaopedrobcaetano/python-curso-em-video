import math

catOposto = float(input('Digite o cateto oposto: '))
catAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = math.sqrt((catOposto * catOposto) + (catAdjacente * catAdjacente))
print('Valor da hipotenusa: {}'.format(hipotenusa))
