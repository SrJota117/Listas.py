import math
area = float(input('Área a ser pintada em m²: '))
litros = area / 3
latas = math.ceil(litros / 18)
custo = latas * 80
print(f'Latas: {latas}, Preço: R${custo:.2f}')

