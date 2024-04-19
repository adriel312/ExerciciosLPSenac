print("M - Masculino F - Feminino")
sexo = input("Qual seu sexo? ")

if sexo == "m":
    altura = float(input("Iforme sua altura: "))
    if altura>=1.70:
        print("Apto ao alistamento!")
    else:
        print("Inapto!")
elif sexo == "f":
    altura = float(input("Iforme sua altura: "))
    if altura>=1.60:
        print("Apto ao alistamento!")
    else:
        print("Inapto!")
else:
    print("Valor não esperado")