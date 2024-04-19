num = int(input("Informe o número: "))
fatorial = num
num -=1
while num>=1:
    fatorial = fatorial*num
    num-=1
print(fatorial)