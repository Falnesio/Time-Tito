# Practical R Exercises in swirl 3

## Introduction to [Swirl](http://www.swirlstats.com)

### lapply and sapply

Essas são as duas principais funções da família de funções chamadas de loop functions ou funções de ciclo. Funções e tal família utiliza da estratégia **Split-Apply-Combine** ou **Separa-Aplica-Junta**. Ou seja elas **Separam** dados em pequenos pedações, **Aplicam** determinada(s) função(ões) a cada pedaço e **Junta** os resultados. Mais informações sobre isso estão no artigo da [Journal of Statistical Software, "The Split-Apply-Combine Strategy for Data Analysis" do Autor Hadley Wickham.](https://www.jstatsoft.org/article/view/v040i01/v40i01.pdf). Utilizaremos o set de dados [Flags da UCI Machine Learning Repository](| http://archive.ics.uci.edu/ml/datasets/Flags
).

Os dados estão na variável **flags**. utilizaremos `head(flags)` e `dim(flags)` pra obtermos uma pequena amostra os dados e ver suas dimensões. Para obter uma descrição mais complesta do set de dados, utiliza-se `viewinfo()`. Para obter a classes de cada vetor no set de dados flags, utilizamos `lapply(flags, class)`.

O "l" de *lapply* significa lista, pois retorna uma lista. Para reduzir a lista a um vetor podemos usar `as.character(cls_list)`. Usar **`sapply`** simplifica esse processo, retornando um vetor ao invés de uma lista com `sapply(flags, class)`. 

Se o resultado de *lapply* for uma lista onde todos os elementos são de tamanho 1, *sapply* retorna um vetor.
Se o resultado de *lapply* for uma lista onde todos os elementos são um vetor de mesmo tamanho, *sapply* retorna uma matriz.
Se *sapply* não souber o que fazer, retorna a mesma coisa que *lapply* retornaria.

Para extrair o número de cores totais em flags, para cada cor, estraímos colunas 11 a 17 e aplicamos sum, pois são colunas onde 1 representa que a bandeira tem tal cor e 0 que não.
```
> head(flag_colors)
  red green blue gold white black orange
1   1     1    0    1     1     1      0
2   1     0    0    1     0     1      0
3   1     1    0    0     1     0      0
4   1     0    1    1     1     0      1
5   1     0    1    1     0     0      0
6   1     0    0    1     0     1      0
> sum(flags$orange)
[1] 26
> flag_colors <- flags[, 11:17]
> lapply(flag_colors, sum)
$red
[1] 153

$green
[1] 91

$blue
[1] 99

$gold
[1] 91

$white
[1] 146

$black
[1] 52

$orange
[1] 26

> sapply(flag_colors, sum)
   red  green   blue   gold  white  black orange 
   153     91     99     91    146     52     26 
   
> # Proporção das cores, (1+1+1+0+0)/5 = média = proporção
> sapply(flag_colors, mean)
      red     green      blue      gold     white     black    orange 
0.7886598 0.4690722 0.5103093 0.4690722 0.7525773 0.2680412 0.1340206 
```

**range()** mostra os valores máximo e mínimo de uma lista ou vetor.

**unique()** retorna um vetor com a primeira instância de cada elemento.
```
> unique(c(3, 4, 5, 5, 5, 6, 6))
[1] 3 4 5 6
```

### vapply and tapply

**vapply()** permite especificar o formato do retorno, se o retorno não for o esperado, *vapply* retorna um erro.
Por exemplo `vapply(flags, unique, numeric(1))` espera que cada elemento retornado seja um vetor numérico de tamanho 1. Por não ser, resultará num erro.
```
Error in vapply(flags, unique, numeric(1)) : values must be length 1,
 but FUN(X[[1]]) result is length 194
```
*sapply* é mais ráapido pra escrever, mas *vapply* é mais seguro, e mais rápido para sets de dados maiores.

**tapply()** serve para quando deseja separar os dados em grupos baseado no valor de uma determinada variável para depois aplicar uma função a cada grupo. `tapply(dados, separados por essa variável, função)`



