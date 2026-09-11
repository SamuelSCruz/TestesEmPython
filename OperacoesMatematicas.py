#Introdução da atividade:
#Cria um algoritimo que solicitamuly ao usuário dois números e imprima na tela a soma, subtração, multiplicação e divisão.
#Variáveis utilizadas: number1 e number2

# Menu: informa as operações e solicita que o usuário informe a que ele deseja
print("\nSoma: 1 | Multiplicaçã: 2 | Subtração: 3 | Divisão: 4\n")
menu = int(input("Informe qual operação deseja realizar: "))


# Condicionais: roda as operações que o usuário deseja.
if menu == 1:
        print("\n********** Soma **********\n")    
        number1 = int(input("Informe o número 1: "))
        number2 = int(input("Informe o número 2: "))
        soma = number1 + number2
        print("\nSoma dos dois números: ", soma,)


elif menu == 2:
    print("\n********** Multiplicação **********\n")
    number1 = int(input("Informe o número 1: "))
    number2 = int(input("Informe o número 2: "))
    mult = number1 * number2
    print(f"\nMultiplicação dos dois números:  {mult}")


elif menu == 3:
    print("\n********** Subtrção **********\n")
    number1 = int(input("Informe o número 1: "))
    number2 = int(input("Informe o número 2: "))
    subt = number1 - number2
    print("\nSubtrção dos dois números: ", subt)


elif menu == 4:
    print("\n********** Divisão **********\n")
    number1 = float(input("Informe o número 1: "))
    number2 = float(input("Informe o número 2: "))
    divs = number1 - number2
    print("\nDivisão dos dois números: ", divs)

else:
     print("\nInforme número conforme no menu\n")