
# Programa que verifica o tipo de triângulo
def tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"
