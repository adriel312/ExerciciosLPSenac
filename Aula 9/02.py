nota = float(input("Informe uma nota: "))

while nota<0 or nota>10:
    print("Nota inválida, insira uma nota entre 0 e 10")
    nota = float(input("Informe uma nota válida: "))

print("Nota inserida com sucesso!")