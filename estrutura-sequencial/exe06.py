# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi, pow

raio = float(input('Raio do circulo: '))

area = pi * pow(raio, 2)

print(f'A aréa do circulo é {area:.2f}.')
