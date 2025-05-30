# Programa que simula um caixa eletrônico
def caixa_eletronico(valor):
    if valor < 10 or valor > 600:
        return "Valor inválido"
    notas = {}
    for n in [100, 50, 10, 5, 1]:
        notas[n] = valor // n
        valor = valor % n
    return notas
