#Introdução da atividade:
#Cria um algoritimo que colete a idade do usuário e informe se é maior ou igual a 18.
#Variáveis utilizadas: idade

idade = int(input("Informe idade: "))

if idade < 18:
        print("\nMenor idade")

elif idade == 18:
        print("\n18 anos!")

else:
        print("\nMaior idade")        