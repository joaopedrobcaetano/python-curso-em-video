from math import sqrt
import random
import emoji

num = int(input('Digite um número para calcular a sua raiz quadrada: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))

print('SORTEIO: O número escolhido é {}.'.format(random.randint(1, 100)))
print(emoji.emojize(':smiling_face_with_sunglasses:'))
print(emoji.emojize('Olá, Mundo! :globe_showing_americas:', language='alias'))
