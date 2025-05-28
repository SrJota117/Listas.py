# Exercício 9
# Programa que escolhe o produto mais barato
preco1 = float(input('Preço do primeiro produto: '))
preco2 = float(input('Preço do segundo produto: '))
preco3 = float(input('Preço do terceiro produto: '))
mais_barato = min(preco1, preco2, preco3)
print('Você deve comprar o que custa:', mais_barato)