'''
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
'''

def convert_celsius_fahrenhiet(celsius):
    return celsius * 1.8 + 32

for i in range(0, 45, 5):
    #celsius = float(input('Entre com uma temperatura (°C): '))
    #if not celsius != 999:
        #break

    fahrenheit = convert_celsius_fahrenhiet(i)

    print(f'{i:.1f}°C = {fahrenheit:.1f}°F')
    
