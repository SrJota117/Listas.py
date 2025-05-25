import math
area = float(input('Área a ser pintada em m²: '))
litros = (area / 6) * 1.1
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
mistura_latas = int(litros // 18)
mistura_galoes = math.ceil((litros - (mistura_latas * 18)) / 3.6)
custo_latas = latas * 80
custo_galoes = galoes * 25
custo_misto = (mistura_latas * 80) + (mistura_galoes * 25)
print(f'Só latas: {latas} - R${custo_latas:.2f}')
print(f'Só galões: {galoes} - R${custo_galoes:.2f}')
print(f'Mistura: {mistura_latas} latas e {mistura_galoes} galões - R${custo_misto:.2f}')
