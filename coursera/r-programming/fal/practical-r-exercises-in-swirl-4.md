# Practical R Exercises in swirl 3

## Introduction to [Swirl](http://www.swirlstats.com)

### Looking at Data 

A primeira coisa que devemos fazer ao obter um conjunto de dados novo é olhar! Qual o formato dos dados? Qauis são as dimensões? Qauis são os nomes das variáveis e onde estão guardadaas? Tem dados faltando, ou algo de errado com os dados?

Vamos usar dados do [United States Department of Agriculture's PLANTS Database](http://plants.usda.gov/adv_search.html).

Ao aplicar `class(plants)`, obtemos `[1] "data.frame"`.

Sabemos abaixo que temos uma tabela com 5166 linhas e 10 colunas.
```
> dim(plants)
[1] 5166   10
> nrow(plants)
[1] 5166
```

Com **object.size()** obtemos quanto espaço ocupa a base de dados
```
> object.size(plants)
644232 bytes
```
Podemos obter os nomes  **names()**.

```
> names(plants)
 [1] "Scientific_Name"      "Duration"             "Active_Growth_Period"
 [4] "Foliage_Color"        "pH_Min"               "pH_Max"              
 [7] "Precip_Min"           "Precip_Max"           "Shade_Tolerance"     
[10] "Temp_Min_F" 
```

Com **head()** obtemos uma amostra das primeiras linhas do conjunto de dados. Por padrão, as primeiras 6 colunas são apresentadas, a não ser se adicionar um argumento identificando ao contrário.

**tail()** é complementar a **head()** porém para o fim do conjunto de dados.

**summary()** dar um resumo dos dados. Para dados numéricos apresenta a quantidade de NAs que aparecem, os quartís, máximo e mínimo; para fatores mostra quantas vezes cada nível aparece na tabela.

Para fatores, quando existem muitos, o restante é colocado como outros **Other**. Para ver o remanescente, utiliza-se `table(conjunto-de-dados$variável-com-fatores)`.

Talvez a funlçao mais útil é `str()`.

### Simulation

Números aleatórios são muito úteis para simulações. Podemos obter uma amostra aleatorizada de uma população com **sample()**. É possível adicionar a probabilidade do aparecimento de cada ítem de uma população com um quarto argumento indicando os valores decimais.

No exemplo abaixo selecionamos e recolocamos aleatoriamente duas bolas de uma sacola 100 vezes, com 0 tendo uma chance de 30% de sair e 1, 70%.
```
> sample(c(0,1), 100, replace = TRUE, prob = c(0.3, 0.7))
  [1] 1 1 1 1 0 0 1 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 1 0 0 1 1 0 0 1 0 0 1 1 1 1
 [37] 0 0 1 1 1 0 0 1 1 0 0 0 1 0 1 1 0 1 1 1 0 1 0 1 1 1 1 1 1 1 0 0 0 1 1 1
 [73] 1 1 1 1 0 1 1 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 0 0 1
```

**replicate(x, f)** serve para replicar uma função f, x vezes, tendo como a saída uma matriz.

**colMeans()** pode ser usado para pegar a média de cada coluna.

**hist()** projeta tais dados num histograma.

### Base Graphics

Gráficos no R. Vamos começar com as bibliotecas já presentes no R. [Alguns dizem que](http://varianceexplained.org/r/teach_ggplot2_to_beginners/) primeiro devemos aprender bibliotecas gráficas mais avançadas como lattice, ggplot2 e ggvis. 

**plot()** tenta retornar o melhor gráfico com os valores e nomes demarcados, plot aqui é outro nome para gráfico de dispersão (scatterplot). Para ver todos os argumentos para `plot()` usamos `?par`.

Para aprender sobre os demais elementos da base gráfica básica, sig esse [link](http://www.ling.upenn.edu/~joseff/rstudy/week4.html).










