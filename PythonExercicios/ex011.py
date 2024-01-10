altura = float(input('Qual é a altura da parede em metros? '))
largura = float(input('Qual é a largura da parede em metros? '))
area = altura * largura
print('A parede tem {} m².'.format(area))
print('Você vai precisar de {} litros de tinta para pintar essa parede.'.format(area / 2))
