# Programa que decompõe um número em centenas, dezenas e unidades
def decompor_numero(num):
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = num % 10
    return f"{centenas} centenas, {dezenas} dezenas e {unidades} unidades"
