# Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.
from math import pow

lado = float(input('Lado do quadrado: '))

area_quad = pow(lado, 2)

dobro = area_quad * 2

print(f'Area do quadrado: {dobro:.2f}cm²')
