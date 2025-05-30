# Programa que calcula as raízes de uma equação do segundo grau
def equacao_segundo_grau(a, b, c):
    if a == 0:
        return "Não é uma equação do segundo grau."
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return f"Raiz única: {x}"
    else:
        import math
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Duas raízes: {x1} e {x2}"
