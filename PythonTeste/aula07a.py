nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:>20}!'.format(nome))

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
produto = num1 * num2
diferenca = num1 - num2
divisao = num1 / num2
potencia = num1 ** num2
divisaoInteira = num1 // num2
resto = num1 % num2
print('A soma é {}, \n o produto é {}, \n a diferença é {}, \n a divisão é {}'.format(soma, produto, diferenca, divisao), end=". ")
print('A potência é {}, \n a divisão inteira é {}, \n o resto é {}'.format(potencia, divisaoInteira, resto))
