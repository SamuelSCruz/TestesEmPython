#Introdução da atividade:
#Cria um algoritimo que solicite ao usuário dois números e informa qual é o maior e qual é o menor
#Variáveis utilizadas: number1 e number2

while True:
        try:
            number1 = int(input("Informe o primeiro número: "))
            number2 = int(input("Informe o segundo número: "))

            if number1 > number2:
                 print("\nNúmero 1 é maior que o número 2!")

            elif number1 == number2:
                 print("\nNúmero 1 é igual ao número 2!")

            elif number2 > number1:
                 print("\nNúmero 1 é maior que o número 2!")

            break

        except ValueError:
            print("\n[ERRO] Informe apenas números!\n\n")


            
