# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Qual valor de sua hora(R$): '))
qtd_hora_mes = int(input('Quantas hora voçê trabalha por mês: '))

salario = valor_hora * qtd_hora_mes

print(f'Seu salario é de R${salario}.')
