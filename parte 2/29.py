print("Carnes disponíveis:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

tipo = input("Escolha o tipo de carne (1, 2 ou 3): ")
quantidade = float(input("Quantidade de carne (Kg): "))
cartao = input("Compra com cartão Tabajara? (s/n): ").lower()

# Define o nome e o preço do kg
if tipo == "1":
    nome_carne = "Filé Duplo"
    preco_kg = 4.90 if quantidade <= 5 else 5.80
elif tipo == "2":
    nome_carne = "Alcatra"
    preco_kg = 5.90 if quantidade <= 5 else 6.80
elif tipo == "3":
    nome_carne = "Picanha"
    preco_kg = 6.90 if quantidade <= 5 else 7.80
else:
    print("Tipo inválido.")
    exit()

# Calcula os valores
preco_total = quantidade * preco_kg
desconto = preco_total * 0.05 if cartao == "s" else 0
valor_final = preco_total - desconto

# Cupom fiscal
print("\nCUPOM FISCAL")
print("Tipo de carne:", nome_carne)
print("Quantidade:", quantidade, "Kg")
print("Preço total: R$", round(preco_total, 2))
print("Tipo de pagamento:", "Cartão Tabajara" if cartao == "s" else "Outro")
print("Desconto: R$", round(desconto, 2))
print("Valor a pagar: R$", round(valor_final, 2))
