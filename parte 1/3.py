notas = [float(input(f'Digite a nota {i+1}: ')) for i in range(4)]
print(sum(notas) / len(notas))
