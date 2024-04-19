nome = input("Insira seu nome: ")
consoante = 0
for letra in nome:
    if letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u":
        consoante += 1
print("O nome",nome,"possui",consoante,"consoantes")