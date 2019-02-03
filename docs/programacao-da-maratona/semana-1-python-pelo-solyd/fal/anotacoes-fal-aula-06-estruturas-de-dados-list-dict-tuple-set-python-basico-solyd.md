# Anotações - Fal - Aula 6 - Estruturas de Dados (List, Dict, Tuple, Set) - Python Básico Solyd.md

 * Programação

1. list
```
lista = []
# Lista ou list (número modificável de ítens ordenados)
lista_nomes = ["Fernando", "Susana"]
```

2. tuple
```
tuple = ()
# Tupla ou tuple (mesmo número finito de dados ordenados e não modificáveis)
tupla_nomes = ("Fernando", "Susana")
	# aceita modificações completas tipo tuplas_nomes = ("Jose", "Maria") 
```

3. dict
```
dicionario = {} ou dicionario = dict()
# Dicionário ou dict (ítens não ordenados divididos por vírgulas, se busca pela categoria)
# dicionários tem keys (categorias) e values (valores) na estrutura keys : values
dicionario_cadastro = {"nome" : "Falnésio", "idade" : 26}
# modificar
dicionario_cadastro["nome"] = "Billy"
# adicionar
dicionario_cadastro["telefone"] = 03134567890
#ver chaves
print(dicionario_cadastro.keys())
```

4. set
```
conjunto = set()
# Conjunto ou set (não tem ítens repetidos e não é ordenado)
# a busca no conjunto pe rápida
conjunto = {"Fal", "Marcela"}
# adicionar
conjunto.add("José")
```

 * Extra
```

# criar múltiplos dicionários

names = []
for i in range(30,35):
    names.append(str(i))
    print(type(i))
for i in names:
    print(type(i))
#names=["lloyd", "alice", "tyler"]
#keys=["homework", "quizzes", "tests"]
steven={ name.capitalize():{key:[] for key in range(5)} for name in names}
print(steven)  

```

# #fim
