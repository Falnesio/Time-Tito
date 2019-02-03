'''
criar múltiplos dicionários
'''
'''
def dicks (length, lista): 
    names = []
    for i in range(length):
        names.append(str(i))
        #print(type(i))
    for i in names:
        #print(type(i))
    keys= lista
    steven={ name.capitalize():{key:[] for key in keys} for name in names}
    print(steven)  

a = dicks(10, ["idade", "raça"])
print(a)

'''
'''
criar múltiplos dicionários pré-definidos
'''
def dicks (lista_nomes, lista_categorias): 
    names = lista_nomes
    keys= lista_categorias
    matrix={ name.capitalize():{key:[] for key in keys} for name in names}
    return matrix  

relatório = dicks (["Bob", "Luana", "João", "Tany", "Matias"], ["Empregos", "Escolaridade", "Cor", "Idade", "Sexo"])
print(relatório)

print(dicks(["joão","paulo", "maria", "fatima"], ["cor", "idade"]))
