'''
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''
n1 = int(input('Entre com um numero inteiro: '))
n2 = int(input('Entre com outro numero inteiro: '))
r1 = float(input('Entre com um numero real: '))

prod = (n1 * 2) * (n2 / 2)
soma = n1 * 3 + r1
terc = pow(r1, 3)

print()
print(f'Produto: {prod:.2f}.')
print(f'Soma: {soma}.')
print(f'Terceiro: {terc:.2f}.')
