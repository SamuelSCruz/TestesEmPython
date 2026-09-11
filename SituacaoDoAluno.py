#Introdução da atividade:
#Cria um algoritimo que solicite ao usuário sua nota e informe se está aprovado, em recuperação ou reprovado.
#Variáveis utilizadas: nota

nota = float(input("Informe sua nota: "))

if nota < 3:
    print("Sua nota: ", nota, "- Reprovado!\n")

elif nota >= 3 and nota <= 7:
    print("Sua nota: ", nota, "- Recuperação!\n")

elif nota > 7 and nota <= 10:
    print("Sua nota: ", nota, "- Aprovado!\n")

else:
    print("Informe nota entre 0 à 10!\n")