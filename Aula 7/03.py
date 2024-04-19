print("1 - Converter de Celsius para Fahrenheit     2 - Converter de Fahrenheit para Celsius")
op_conversao = int(input("Informe o tipo de conversão: "))

match op_conversao:
    case 1:
        celsius = float(input("Informe a temperatura em Celsius: "))
        print(celsius,"C equivale a",(celsius * 9/5) + 32,"F")
    case 2:
        fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
        print(fahrenheit,"F equivale a",(fahrenheit - 32) * 5/9,"C")
    case _:
        print("Opção inválida!")