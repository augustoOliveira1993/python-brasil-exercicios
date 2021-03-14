# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# Formula: C = 5 * ((F-32) / 9).
temp_fahren = float(input('Entre com uma temperatura (°F): '))

celsius = 5 * ((temp_fahren-32) / 9)

print(f'{temp_fahren:.1f}°F pra celsius {celsius:.1f}°C.')
