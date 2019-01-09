# https://wiki.python.org.br/EstruturaDeDecisao
import math
print("")
print("Para as inserções de numeros nos programas utilize pontos e não vírgulas.")
print("")
questao = int(input("Qual questão quer abrir? "))
print("")

# 1
if questao == 1:
    print("Maior número de dois")
    lista1 = [0, 0]
    lista1[0] = float(input("Primeiro Número: "))
    lista1[1] = float(input("Segundo Número: "))
    print(max(lista1))
# 2
if questao == 2:
    print("Positivo ou Negativo")
    a2 = float(input("Digita um número: "))
    if a2 > 0:
        print(a2, "é positivo.")
    elif a2 == 0:
        print(a2, "não é negativo ou positivo.")
    else:
        print(a2, "é negativo.")
# 3
if questao == 3:
    print("F ou M?")
    a3 = input("Escreva F ou M: ")
    if a3 == 'F':
        print("F - Feminino")
    elif a3 == 'M':
        print("M - Masculino")
    else:
        print("Assertou misseravi!")
# 4
if questao == 4:
    print("Consoante ou Vogal?")
    lista4 = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    a4 = input("Digite uma letra:")
    if a4 in lista4:
        print("É vogal!")
    else:
        print("É consoante!")
# 5
if questao == 5:
    print("Passou de ano?")
    a5 = float(input("Primeira nota (0-10): "))
    b5 = float(input("Segunda nota (0-10): "))
    media = (a5 + b5) / 2
    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
# 6
if questao == 6:
    print("Maior número de três")
    lista6 = [0, 0, 0]
    lista6[0] = float(input("Primeiro Número: "))
    lista6[1] = float(input("Segundo Número: "))
    lista6[2] = float(input("Terceiro Número: "))
    print("Maior:", max(lista6))
# 7
if questao == 7:
    print("Maior e Menor número de três")
    lista7 = [0, 0, 0]
    lista7[0] = float(input("Primeiro Número: "))
    lista7[1] = float(input("Segundo Número: "))
    lista7[2] = float(input("Terceiro Número: "))
    print("Maior:", max(lista7), "; Menor:", min(lista7))
# 8
if questao == 8:
    print("Qual o produto mais barato?")
    print("Digite os preços dos produtos.")
    lista8 = {'Primeiro produto': 0, 'Segundo produto': 0, 'Terceiro produto': 0}
    lista8['Primeiro produto'] = float(input("Primeiro produto: "))
    lista8['Segundo produto'] = float(input("Segundo produto: "))
    lista8['Terceiro produto'] = float(input("Terceiro produto: "))
    for i in lista8.keys():
        if lista8[i] == min(lista8.values()):
            print("Melhor produto:", i)
# 9
if questao == 9:
    print("Ordem Decrescente")
    lista9 = input("Escreva três números separados por espaços: ").split(" ")
    lista9 = [float(x) for x in lista9]
    lista9 = sorted(lista9, key=float)
    print(lista9)
# 10
if questao == 10:
    print("Qual o seu turno?")
    a10 = input("Em qual turno estuda: matutino (m), verspertino (v) ou noturno (n)? ")
    lista10 = {'m': 'Bom Dia!', 'v': 'Boa Tarde!', 'n': 'Boa Noite!'}
    existe10 = False
    for i in lista10.keys():
        if a10 == i:
            print(lista10[i])
            existe10 = True
    if existe10 is False:
        print("Valor inválido!")
# 11
if questao == 11:
    print("Aumentos Tabajara")
    a11 = float(input("Qual o seu salário atual? "))
    aumento11 = 0
    if a11 <= 280:
        aumento11 = 0.2
    elif a11 <= 700:
        aumento11 = 0.15
    elif a11 <= 1500:
        aumento11 = 0.10
    elif a11 > 1500:
        aumento11 = 0.05
    print("Salário anterior:", a11)
    print("Aumento:", aumento11 * 100, "%")
    print("Valor do aumento:", aumento11 * a11)
    print("Salário atual", a11 * (1+aumento11))
# 12
if questao == 12:
    print("Impostos")
    a15 = float(input("Digite o quanto ganha por hora: "))
    b15 = float(input("Digite quantas horas trabalha no mês: "))
    salario15 = a15 * b15
    salario_bruto15 = salario15
    print("+ Salário Bruto : R$", salario15)
    if salario15 <= 1999.18:
        print("- IR : Isento")
    elif salario15 <= 2967.98:
        print("- IR (7.5%) : R$", salario15 * 0.075)
        salario_bruto15 -= salario15 * 0.075
    elif salario15 <= 3938.60:
        print("- IR (15%) : R$", salario15 * 0.15)
        salario_bruto15 -= salario15 * 0.15
    elif salario15 <= 4897.91:
        print("- IR (22.5%) : R$", salario15 * 0.225)
        salario_bruto15 -= salario15 * 0.225
    else:
        print("- IR (27.5%) : R$", salario15 * 0.275)
        salario_bruto15 -= salario15 * 0.275
    if salario15 <= 1693.72:
        print("- INSS (8%) : R$", salario15 * 0.08)
        salario_bruto15 -= salario15 * 0.08
    elif salario15 <= 2822.90:
        print("- INSS (9%) : R$", salario15 * 0.09)
        salario_bruto15 -= salario15 * 0.09
    elif salario15 <= 5645.80:
        print("- INSS (11%) : R$", salario15 * 0.11)
        salario_bruto15 -= salario15 * 0.11
    else:
        print("- INSS : Isento")
    print("FGTS (11%) : R$", salario15 * 0.11)
    print("= Salário Líquido : R$", salario_bruto15)
# 13
if questao == 13:
    print("Dia da semana")
    a13 = int(input("Digite um número de 1 a 7: "))
    lista13 = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    if a13 in lista13.keys():
        print(lista13[a13])
    else:
        print("valor inválido")
# 14
if questao == 14:
    a14 = input("Digite suas duas notas (0-10) separadas por espaço: ").split(" ")
    a14 = [float(x) for x in a14]
    print("Notas:", a14)
    media = sum(a14)/len(a14)
    print("Média", media)
    if media <= 4:
        print("Conceito E, REPROVADO")
    elif media <= 6:
        print("Conceito D, REPROVADO")
    elif media <= 7.5:
        print("Conceito C, APROVADO")
    elif media <= 9:
        print("Conceito B, APROVADO")
    else:
        print("Conceito A, APROVADO")
# 15
if questao == 15:
    print("Triângulos")
    a15 = input("Digite très números separadas por espaços: ").split(" ")
    a15 = [float(x) for x in a15]
    a15 = sorted(a15, key = float)
    if a15[2] > a15[0] + a15[1]:
        print("Não é Triângulo!")
    elif a15[0] == a15[1] == a15[2]:
        print("Triângulo Equilátero")
    elif a15[0] == a15[1] or a15[1] == a15[2] or a15[0] ==  a15[2]:
        print("Triângulo Isósceles")
    elif a15[0] + a15[1] == a15[2]:
        print("É uma reta!")
    else:
        print("Triângulo Escaleno")
# 16
if questao == 16:
    print("Equação de Segundo Grau")
    print("ax² + bx + c")
    a16 = float(input("Insira o 'a' de ax²: (x²)*"))
    if a16 == 0:
        print("Não é equação de terceiro grau!")
        exit()
    b16 = float(input("Insira o 'b' de bx :  (x)*"))
    c16 = float(input("Insira o 'c' de c  :      "))
    delta16 = (b16 ** 2) - 4 * a16 * c16
    if delta16 < 0:
        print("Equação não possui raízes reais!")
        exit()
    elif delta16 == 0:
        raiz16 = (- b16) / (2 * a16)
        print("A equação possui apenas uma raíz real:", raiz16)
    else:
        raiza16 = - b16 + math.sqrt(delta16)
        raizb16 = - b16 - math.sqrt(delta16)
        print("As raízes são:", raiza16, "e", raizb16)
# 17
if questao == 17:
    print("Ano Bisexto")
    a17 = int(input("Digite um ano: "))
    if a17 % 4 == 0:
        print("É ano bisexto!")
    else:
        print("Não é ano bisexto!")
# 18
if questao == 18:
    print("Data é válida?")
    a18 = input("Insira data no seguinte formato dd/mm/aaaa:\n").split("/")
    a18 = [int(x) for x in a18]
    if a18[1] > 12 or a18[1] < 1 or a18[0] > 31 or a18[0] < 1:
        print("Data inválida!")
        exit()
    if a18[2] % 4 != 0:
        calendario18 = { 1: 31,
                         2: 28,
                         3: 31,
                         4: 30,
                         5: 31,
                         6: 30,
                         7: 31,
                         8: 31,
                         9: 30,
                         10: 31,
                         11: 30,
                         12: 31
                         }
    else:
        calendario18 = { 1: 31,
                         2: 29,
                         3: 31,
                         4: 30,
                         5: 31,
                         6: 30,
                         7: 31,
                         8: 31,
                         9: 30,
                         10: 31,
                         11: 30,
                         12: 31
                         }
    if a18[0] <= calendario18[a18[1]]:
        print("Data Válida!")
# 19
if questao == 19:
    print("Centenas, Dezenas e Unidades")
    try:
        a19 = input("Digite um número inteiro menor que 1000 e maior que 0: ")
        number19 = int(a19)
        a19 = list(a19)
        a19 = [int(x) for x in a19]
        if number19 > 1000 or number19 < 1:
            print("Valor inválido!")
        else:
            if a19[0] == 1:
                pop1 = "1 centena "
            else:
                pop1 = str(a19[0])+" centenas "
            if a19[1] == 1:
                pop2 = "1 dezena"
            else:
                pop2 = str(a19[1])+" dezenas "
            if a19[2] == 1:
                pop3 = "e 1 unidade "
            else:
                pop3 = "e "+str(a19[2])+" unidades "
            print(pop1 + pop2 + pop3)
    except Exception as e:
        print("Valor inválido!", e)
# 20
if questao == 20:
    print("Média de três notas")
    a5 = float(input("Primeira nota (0-10): "))
    b5 = float(input("Segunda nota (0-10): "))
    c5 = float(input("Terceira nota (0-10): "))
    media = (a5 + b5 + c5) / 2
    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado, nota", media)
    else:
        print("Reprovado, nota", media)
# 21
if questao == 21:
    print("Caixa Eletrônico")
    a21 = float(input("Quanto gostaria de sacar (10-600)? "))
    inicio21 = a21
    def faz21(d21, c21):
        b21 = d21 / c21 - ((d21 % c21)/ c21)
        return int(b21)
    def altera_a21(d21, c21, nota):
        d21 = d21 - (nota * c21)
        return d21
    def vira_str(numero21):
        lista_de_numeros = ['zero notas', 'uma nota', 'duas notas', 'três notas', 'qautro notas', 'cinco notas', 'seis notas', 'sete notas', 'oito notas', 'nove notas', 'dez notas']
        return lista_de_numeros[numero21]
    nota_100 = faz21(a21, 100)
    a21 = altera_a21(a21, 100, nota_100)
    nota_100 = vira_str(nota_100)
    nota_50 = faz21(a21, 50)
    a21 = altera_a21(a21, 50, nota_50)
    nota_50 = vira_str(nota_50)
    nota_10 = faz21(a21, 10)
    a21 = altera_a21(a21, 10, nota_10)
    nota_10 = vira_str(nota_10)
    nota_5 = faz21(a21, 5)
    a21 = altera_a21(a21, 5, nota_5)
    nota_5 = vira_str(nota_5)
    nota_1 = faz21(a21, 1)
    a21 = altera_a21(a21, 1, nota_1)
    nota_1 = vira_str(nota_1)
    print("Para sacar a quantia de", inicio21,"reais, o programa fornece"
          ,nota_100 ,"de 100,", nota_50,"de 50,", nota_10,"de 5 e", nota_1,"de 1.")
# 22
if questao == 22:
    print("Impar ou Par")
    a22 = int(input("Digite um número inteiro: "))
    if a22 % 2 == 0:
        print("É par!")
    else:
        print("É impar!")
# 23
if questao == 23:
    print("Inteiro ou Decimal")
    a23 = input("Digite um número: ")
    a23 = float(a23)
    if round(a23) == a23:
        a23 = int(a23)
    else:
        a23 = float(a23)
    if isinstance(a23, int):
        print("É inteiro")
    else:
        print("É decimal")
# 24
if questao == 24:
    print("Caculadora")
    a24 = input("Primeiro número: ")
    b24 = input("Segundo número: ")
    c24 = input("Qual operação deseja fazer?\nSoma (s+), multiplicação (m), subtração (s-), divisão (d)\n")
    operações24 = {'s+': '+', 's-': '-', 'm': '*', 'd': '/'}
    exec('resultado24 = '+ a24 + operações24[c24] + b24)
    print("resultado:", resultado24)
    def q2(a2):
        if a2 > 0:
            print(a2, "é positivo.")
        elif a2 == 0:
            print(a2, "não é negativo ou positivo.")
        else:
            print(a2, "é negativo.")
    def q22(a22):
        if a22 % 2 == 0:
            print("É par!")
        else:
            print("É impar!")
    def q23(a23):
        a23 = float(a23)
        if round(a23) == a23:
            a23 = int(a23)
        else:
            a23 = float(a23)
        if isinstance(a23, int):
            print("É inteiro!")
        else:
            print("É decimal!")
    q2(resultado24)
    q22(resultado24)
    q23(resultado24)

# 25
if questao == 25:
    print("Criminosos?")
    print("Interrogue a pessoa, insira (s) sim ou (n) não:")
    lista25 = ["Telefonou para a vítima? ",
               "Esteve no local do crime? ",
               "Mora perto da vítima? ",
               "Devia para a vítima? ",
               "Já trabalhou com a vítima? "]
    dic25 = {0: 'Inocente!',
              1: 'Inocente!',
              2: 'Cúmplice!',
              3: 'Cúmplice!',
              4: 'Cúmplice!',
              5: "Assassino!"}
    pontos25 = 0
    for i in lista25:
        r25 = input(i)
        if r25 == 's':
            pontos25 +=1
    print("O sujeito é",dic25[pontos25])
# 26
if questao == 26:
    print("Posto de Gasolina")
    a26 = float(input("Quantidade de álcool em litros vendidos: "))
    b26 = float(input("Qauntidade de gasolina em litros vendidos: "))
    if a26 > 20:
        preco_a26 = (a26 * 1.90) - (a26 * 0.05)
    else:
        preco_a26 = (a26 * 1.90) - (a26 * 0.03)
    if b26 > 20:
        preco_b26 = (b26 * 2.50) - (b26 * 0.06)
    else:
        preco_b26 = (b26 * 2.50) - (b26 * 0.04)
    print("Alcool: R$", preco_a26)
    print("Gasolina: R$", preco_b26)
# 27

