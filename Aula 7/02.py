nota_1 = float(input("Informe o valor da nota 1: "))
nota_2 = float(input("Informe o valor da nota 2: "))

media = (nota_1 + nota_2)/2

if media>=9 and media<=10:
    print("Conceito A")
elif media>=7.5 and media<9:
    print("Conceito B")
elif media>=6 and media<7.5:
    print("Conceito C")
elif media>=4 and media<6:
    print("Conceito D")
elif media>=0 and media<4:
    print("Conceito E")