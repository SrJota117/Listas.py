litros = float(input("Quantos litros foram vendidos? "))
tipo = input("Tipo de combustível (A para álcool, G para gasolina): ").upper()

if tipo == "A":
    preco_litro = 1.90
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo == "G":
    preco_litro = 2.50
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo de combustível inválido.")
    exit()

preco_total = litros * preco_litro
valor_desconto = preco_total * desconto
valor_final = preco_total - valor_desconto

print("Valor a ser pago: R$", round(valor_final, 2))
