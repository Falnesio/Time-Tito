# https://wiki.python.org.br/EstruturaDeDecisao
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
#14
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

