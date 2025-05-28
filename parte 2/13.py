# Programa de cálculo de folha de pagamento
hora = float(input('Valor da hora: '))
horas = float(input('Horas trabalhadas: '))
bruto = hora * horas
if bruto <= 900:
    ir = 0
elif bruto <= 1500:
    ir = 0.05
elif bruto <= 2500:
    ir = 0.10
else:
    ir = 0.20
inss = 0.10
fgts = 0.11
print(f'Salário Bruto: R${bruto:.2f}')
print(f'IR: R${bruto * ir:.2f}')
print(f'INSS: R${bruto * inss:.2f}')
print(f'FGTS: R${bruto * fgts:.2f}')
print(f'Salário Líquido: R${bruto - (bruto * ir + bruto * inss):.2f}')