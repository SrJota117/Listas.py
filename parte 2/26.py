respostas = 0

p1 = input("Telefonou para a vítima? (s/n) ").lower()
if p1 == "s":
    respostas += 1

p2 = input("Esteve no local do crime? (s/n) ").lower()
if p2 == "s":
    respostas += 1

p3 = input("Mora perto da vítima? (s/n) ").lower()
if p3 == "s":
    respostas += 1

p4 = input("Devia para a vítima? (s/n) ").lower()
if p4 == "s":
    respostas += 1

p5 = input("Já trabalhou com a vítima? (s/n) ").lower()
if p5 == "s":
    respostas += 1

if respostas == 2:
    print("Suspeita")
elif 3 <= respostas <= 4:
    print("Cúmplice")
elif respostas == 5:
    print("Assassino")
else:
    print("Inocente")
