exercícios de Python, começando do zero e usando somente os conteúdos que vimos até agora:

Variáveis
Tipos int, float e str
print()
input()
int() e float()
Operadores matemáticos
Operadores de comparação
if, elif e else
Indentação
for + range()
while
Funções com def e return
Comentários
f-strings

Vou evitar listas, dicionários, classes, módulos, tratamento de exceções etc. por enquanto.

🐍 Atividade 1 — Variáveis e print()

Crie um programa que armazene:

seu nome;
sua idade;
sua cidade;
seu curso.

Depois, exiba todas essas informações na tela.

Exemplo de saída:

Nome: Samuel
Idade: 20
Cidade: Salvador
Curso: Análise e Desenvolvimento de Sistemas
🐍 Atividade 2 — Operações matemáticas

Crie duas variáveis:

numero1 = 20
numero2 = 5

Calcule e exiba:

Soma
Subtração
Multiplicação
Divisão

Desafio: faça o programa mostrar o nome da operação junto com o resultado.

🐍 Atividade 3 — Entrada de dados

Faça um programa que pergunte ao usuário:

Digite seu nome:
Digite sua idade:

Depois mostre:

Olá, Samuel!
Você tem 20 anos.

Utilize input().

Importante: transforme a idade em int.

🐍 Atividade 4 — Calculadora simples

Peça ao usuário dois números.

Depois mostre:

Soma:
Subtração:
Multiplicação:
Divisão:

Utilize:

input()
float()
print()
🐍 Atividade 5 — Maior de idade

Peça a idade do usuário.

Se a idade for maior ou igual a 18:

Maior de idade

Caso contrário:

Menor de idade

Utilize apenas:

if
else
🐍 Atividade 6 — Situação do aluno

Peça a nota de um aluno.

Utilize as seguintes regras:

Nota maior ou igual a 7 → Aprovado
Nota maior ou igual a 5 → Recuperação
Nota menor que 5 → Reprovado

Utilize:

if
elif
else
🐍 Atividade 7 — Comparação de números

Peça dois números ao usuário.

Informe qual é:

o maior;
o menor;

Caso sejam iguais, informe:

Os números são iguais.
🐍 Atividade 8 — Contagem com for

Faça um programa que mostre os números de 1 até 10.

Utilize:

for
range()

Resultado esperado:

1
2
3
4
5
6
7
8
9
10
🐍 Atividade 9 — Tabuada

Peça um número ao usuário e mostre a tabuada dele de 1 até 10.

Por exemplo, se o usuário digitar 5:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Utilize for e range().

🐍 Atividade 10 — Contagem com while

Crie um programa que comece com:

contador = 1

E mostre os números de 1 até 10 utilizando while.

🐍 Atividade 11 — Função de soma

Crie uma função chamada:

calcular_soma()

Ela deve receber dois números e retornar a soma deles.

Depois utilize a função para calcular:

10 + 20
🐍 Atividade 12 — Função para verificar nota

Crie uma função chamada:

verificar_nota()

Ela deve receber uma nota e retornar:

"Aprovado" se a nota for ≥ 7;
"Recuperação" se a nota for ≥ 5;
"Reprovado" se for < 5.

Depois, peça a nota ao usuário e utilize a função.

🎯 Desafio final

Agora vamos juntar praticamente tudo.

Crie um programa que:

Pergunte o nome do aluno.
Pergunte a nota 1.
Pergunte a nota 2.
Calcule a média.
Informe a situação:
média ≥ 7 → Aprovado
média ≥ 5 → Recuperação
média < 5 → Reprovado
Mostre tudo utilizando f-string.

Exemplo:

Digite seu nome: Samuel
Digite a primeira nota: 8
Digite a segunda nota: 6

Aluno: Samuel
Média: 7.0
Situação: Aprovado

Sugestão: tente resolver primeiro sem olhar exemplos de código. Se travar em alguma atividade, pode me mandar seu código, e eu corrijo explicando linha por linha, sem avançar para conteúdos que ainda não estudamos.
