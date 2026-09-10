"""
Algoritmo que armazena dados do usuário e imprime na tela.
Variáveis utilizadas: nome, idade, cidade, curso
"""

#Introdução da atividade:
#Cria um algoritimo que armazene dados do usuario e imprima na tela.
#Variáveis utilizadas: nome, idade, cidade, curso

nome = input("Informe seu nome: ")

# Tratamento de exceção, usuário deve informar apenas números.
while True: # O while True mantém o programa pedindo a entrada até que seja válida. 

    # |Try e Except são usados para tratar erros (também chamados de exceções).     |
    # |Isso significa que você pode escrever código que continua funcionando mesmo  |
    # |quando acontece algum problema inesperado, em vez de o programa simplesmente |
    # |parar com uma mensagem de erro.                                              |

#                        Como funciona:
# Try: você coloca dentro dele o código que pode gerar um erro.
    try: # O try tenta converter a entrada para inteiro.
        idade = int(input("Informe sua idade: ")) # Captura do idade do usuário.
        break # Sai do loop se informação for bem sucedida

# Except: aqui você define o que deve acontecer caso o erro ocorra.
    except ValueError: # Se o usuário digitar algo que não seja número, o except ValueError captura o erro e mostra uma mensagem amigável.
        print("\n[ERRO]Informe apenas números!")

cidade = input("Informe cidade: ")


# Informações que serão impressas
print("\nMeu nome: ", nome)
print("Minha idade: ", idade)
print("Minha cidade: ", cidade)


