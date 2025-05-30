# Programa que calcula a média de 3 notas
def media_notas(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media == 10:
        return f"Aprovado com Distinção, média: {media}"
    elif media >= 7:
        return f"Aprovado, média: {media}"
    else:
        return f"Reprovado, média: {media}"
