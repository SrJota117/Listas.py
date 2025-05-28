# Exercício 12# Programa que calcula aumento salarial
salario = float(input('Digite o salário: '))
if salario <= 280:
    perc = 0.20
elif salario <= 700:
    perc = 0.15
elif salario <= 1500:
    perc = 0.10
else:
    perc = 0.05
aumento = salario * perc
novo_salario = salario + aumento
print('Salário antes:', salario)
print('Percentual:', perc * 100, '%')
print('Aumento:', aumento)
print('Novo salário:', novo_salario)