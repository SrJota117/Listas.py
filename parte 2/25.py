num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Opção: ")

if opcao == "1":
    resultado = num1 + num2
elif opcao == "2":
    resultado = num1 - num2
elif opcao == "3":
    resultado = num1 * num2
elif opcao == "4":
    if num2 == 0:
        print("Divisão por zero.")
        exit()
    resultado = num1 / num2
else:
    print("Opção inválida.")
    exit()

print("Resultado:", resultado)

if resultado == int(resultado):
    print("É inteiro.")
else:
    print("É decimal.")

if resultado >= 0:
    print("É positivo.")
else:
    print("É negativo.")

if resultado == int(resultado):
    if int(resultado) % 2 == 0:
        print("É par.")
    else:
        print("É ímpar.")
1