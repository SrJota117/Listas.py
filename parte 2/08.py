# Programa que lê 3 números e mostra o maior e o menor
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print('Maior número:', maior)
print('Menor número:', menor)