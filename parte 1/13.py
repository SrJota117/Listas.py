peso = float(input('Digite o peso de peixes: '))
excesso = max(0, peso - 50)
multa = excesso * 4
print(f'Excesso: {excesso}kg, Multa: R${multa:.2f}')

