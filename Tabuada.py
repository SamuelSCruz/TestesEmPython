#Introdução da atividade:
#Cria um algoritimo que solicita ao usuário um número e ele é exibido como uma tabuada.
#Variáveis utilizadas: number


print("**************** TABUADA ****************\n")
print("\nSoma: 1 | Multiplicaçã: 2 | Subtração: 3 | Divisão: 4\n")
menu = int(input("Informe qual operação deseja realizar: "))

match menu: # Escolha(match): Menu para usuário decidir qual operação quer. 
    case 1: # Caso(case) o usário escolha(match) o número 1, ele irá irá escolher o número que será somado na tabuáda
        while True:
            try:
                number = int(input("Informe um número: ")) # Solicita o número
                for i in range(1,11): # Laço de repetição que irá imprimir 10x de 1 à 11
                    print(f"{number} + {i} = {number + i}") # Imprime o resultado. Sem o f (do jeito antigo com vírgulas): |print(number,(" + "), i,(" = "), number + i)|
                    break
            except ValueError:
                print("[ERRO] Informe um número!\n")

    case 2: 
        while True:
            try:
                number = int(input("Informe um número: ")) 
                for i in range(1,11):
                    print(f"{number} x {i} = {number * i}")
                    break
            except ValueError:
                print("[ERRO] Informe um número!\n")

    case 3: 
        while True:
            try:
                number = int(input("Informe um número: ")) 
                for i in range(1,11):
                    print(f"{number} - {i} = {number - i}")
                    break
            except ValueError:
                print("[ERRO] Informe um número!\n")

    case 4: 
        while True:
            try:
                number = int(input("Informe um número: ")) 
                for i in range(1,11):
                    print(f"{number} / {i} = {number / i}")
                    break
            except ValueError:
                print("[ERRO] Informe um número!\n")

