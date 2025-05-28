# Programa que mostra 3 números em ordem decrescente
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
nums = [num1, num2, num3]
nums.sort(reverse=True)
print('Números em ordem decrescente:', nums)