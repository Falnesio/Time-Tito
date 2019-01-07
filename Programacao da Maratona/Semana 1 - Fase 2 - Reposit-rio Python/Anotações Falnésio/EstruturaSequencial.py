# https://wiki.python.org.br/EstruturaSequencial
print("")
print("Para as inserções de numeros nos programas utilize pontos e não vírgulas.")
print("")
questao = int(input("Qual questão quer abrir? "))
print("")

# 1
if questao == 1:
    print("Alo mundo")
# 2
if questao == 2:
    numero2 = str(input("Digite um número: "))
    print("O número informado foi", numero2+".")
# 3
if questao == 3:
    print("Vamos somar?")
    a3 = float(input("Digite o primeiro número: "))
    b3 = float(input("Digite o segundo número: "))
    print("Resposta:", a3 + b3)
# 4
if questao == 4:
    print("Notas bimestrais!")
    i4 = 1
    lista4 = []
    while i4 < 5:
        i4 = str(i4)
        r4 = float(input("Digite nota "+i4+": "))
        lista4.append(r4)
        i4 = int(i4)
        i4 += 1
    print("Média:", sum(lista4)/len(lista4))
# 5
if questao == 5:
    print("Metros para centímetros")
    numero5 = float(input("Digite quantos metros: "))
    print(numero5 * 100, "centímetros")
# 6
if questao == 6:
    print("Área do círculo pelo raio")
    numero6 = float(input("Digite o raio: "))
    print("A área do círculo é", 3.14*numero6*numero6)
# 7
if questao == 7:
    print("Dobro da área de um quadrado")
    numero7 = float(input("Digite o tamanho do lado do quadrado: "))
    print(numero7 * numero7 * 2)
# 8
if questao == 8:
    print("Salário Mensal")
    a8 = float(input("Digite o quanto ganha por hora: "))
    b8 = float(input("Digite quantas horas trabalha no mês: "))
    print("R$", a8 * b8)
# 9
if questao == 9:
    print("Transformar Farenheit em Celcius")
    numero9 = float(input("Digite o número da temperatura em Farenheit: "))
    print((5 * (numero9 - 32) / 9), "Celcius")
# 10
if questao == 10:
    print("Transformar Celcius em Farenheit")
    numero9 = float(input("Digite o número da temperatura em Celcius: "))
    print(((numero9 * 9/5) + 32), "Farenheit")
# 11
if questao == 11:
    lista11 = []
    i11 = 0
    while i11 < 3:
        lista11.append(float(input()))
        i11 += 1
    print("a.", (lista11[0] * 2) * (lista11[1] / 2))
    print("b.", (lista11[0] * 3) + (lista11[2]))
    print("c.", lista11[2] ** 3)
# 12
if questao == 12:
    print("Calcule seu peso ideal")
    numero12 = float(input("Digite a sua altura: "))
    print((72.7*numero12) - 58)
# 13
if questao == 13:
    print("Calcule seu peso ideal h/m")
    a = input("Você é homem (h) ou mulher (m)? ")
    if a == "h":
        numero13 = float(input("Homem, digite a sua altura: "))
        print((72.7 * numero13) - 58)
    else:
        numero13 = float(input("Mulher, digite a sua altura: "))
        print((62.1 * numero13) - 44.7)
# 14
if questao == 14:
    print("Excesso de Peixe")
    numero14 = float(input("Quantos kilos de peixe pegou? "))
    if numero14 > 50:
        print("Multa R$", (numero14 - 50) * 4)
    else:
        print("Sem multa")
        print("Peso:", numero14, "kilos")
# 15
if questao == 15:
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
    print("- Sindicato (5%) : R$", salario15 * 0.05)
    salario_bruto15 -= salario15 * 0.05
    print("= Salário Líquido : R$", salario_bruto15)
# 16
if questao == 16:
    print("Comprar tinta")
    numero16 = float(input("Quantos metros quadrados serão pintados? "))
    litros_de_tinta16 = 1 / 3 * numero16
    if litros_de_tinta16 % 18 != 0:
        latas16 = (litros_de_tinta16 - (litros_de_tinta16 % 18)) / 18 + 1
    else:
        latas16 = litros_de_tinta16 / 18
    print("Terá que comprar", latas16, "latas e gastar R$", latas16 * 80)
# 17
if questao == 17:
    print("Comprar tinta")
    numero16 = float(input("Quantos metros quadrados serão pintados? "))
    litros_de_tinta16 = 1 / 6 * numero16
    if litros_de_tinta16 % 18 != 0:
        latas16 = (litros_de_tinta16 - (litros_de_tinta16 % 18)) / 18 + 1
    else:
        latas16 = litros_de_tinta16 / 18
    print("Terá que comprar", latas16, "latas de 18 litros e gastar R$", latas16 * 80)
    print("ou")
    if litros_de_tinta16 % 3.6 != 0:
        latas16 = (litros_de_tinta16 - (litros_de_tinta16 % 3.6)) / 3.6 + 1
    else:
        latas16 = litros_de_tinta16 / 3.6
    print("Terá que comprar", latas16, "galões de 3.6 litros e gastar R$", latas16 * 25)
    print("ou")
    if litros_de_tinta16 % 18 != 0:
        if litros_de_tinta16 % 18 <= 10.8:
            latas16 = (litros_de_tinta16 - (litros_de_tinta16 % 18)) / 18
            if (litros_de_tinta16 % 18) % 3.6 != 0:
                galoes16 = (litros_de_tinta16 % 18 - (litros_de_tinta16 % 18 % 3.6)) / 3.6 + 1
            else:
                galoes16 = litros_de_tinta16 % 18 / 3.6
        else:
            latas16 = (litros_de_tinta16 - (litros_de_tinta16 % 18)) / 18 + 1
            galoes16 = 0
    else:
        latas16 = litros_de_tinta16 / 18
        galoes16 = 0
    print("Terá que comprar", latas16, "latas de 18 litros e", galoes16,
          " galões de 3,6 litros, gastando R$", latas16 * 80 + galoes16 * 25)
# 18
if questao == 18:
    print("Demora para Download")
    a18 = float(input("Digite o tamanho do arquivo em MB: "))
    b18 = float(input("Digite a velocidade da internet em MBps: "))
    segundos = a18 / b18
    print("Irá demorar", segundos / 60, "minutos para baixar", a18, "MB com", b18, "MBps.")
# fim
