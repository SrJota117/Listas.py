ganho_hora = float(input('Quanto você ganha por hora? '))
horas = float(input('Horas trabalhadas: '))
bruto = ganho_hora * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print(f'+ Salário Bruto : R${bruto:.2f}\n- IR : R${ir:.2f}\n- INSS : R${inss:.2f}\n- Sindicato : R${sind:.2f}\n= Salário Líquido : R${liquido:.2f}')
