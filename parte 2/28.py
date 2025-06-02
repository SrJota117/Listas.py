morango_kg = float(input("Quantos Kg de morango? "))
maca_kg = float(input("Quantos Kg de maçã? "))

# Preços por Kg
if morango_kg <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if maca_kg <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

# Cálculo do valor total
total_kg = morango_kg + maca_kg
total_valor = (morango_kg * preco_morango) + (maca_kg * preco_maca)

# Verifica se tem direito ao desconto
if total_kg > 8 or total_valor > 25:
    total_valor *= 0.9  # aplica 10% de desconto

print("Valor a pagar: R$", round(total_valor, 2))
