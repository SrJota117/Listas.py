# Programa que mostra o dia da semana
dia = int(input('Digite um número (1-7): '))
dias = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
print(dias.get(dia, 'Valor inválido'))