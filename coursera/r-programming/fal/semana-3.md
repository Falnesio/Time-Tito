# Anotações Fal

## R Programming

### Semana 3 - Ciclos

Nessa semana vou aprender sobre funções *loop* e como utilizar o debugger; como definir uma função anônima (**anonimous function** ou função sem nome) e descrever seu uso em funçoes loop; descrever como ativar o debugger do R para uma função arbitrária; e descrever o que a função **traceback()** faz e o que e a **function call stack**.

#### Loop Functions - Funções de Ciclos

Tais funções facilita muito trabalhos repetitivos, especialmente na linha de comando no console ou terminal.

**lapply()**: Cicla por uma lista e aplica a função a cada elemento

**sapply()**: Mesmo que lapply, porém tenta simplificar o resultado, por exemplo ter a saída de um vetor ao invés de uma lista (quando possível).

**apply()**: Aplica a função nas margens de um **array** (**arranjo**). Colapsa arrays.

**tapply()**: Aplica a função nos subconjuntos de um vetor. Aplica fatores.

**mapply()**: Versão multivariada de *lapply()*. Aplica mais argumentos a mais vetores. Faz funções que não aceitam vetores, aceitarem.

A função auxiliar **split()** é útil, particulamente em conjunto com lapply, pois divide objetos em sub-peças.

##### lapply()

3 argumentos: uma lista x, uma função (ou o nome de uma função), etc.
Se x não for uma lista, é aplicado as.list(x) automaticamente

O ciclo real ocorre internamente em código C. A saída sempre será uma lista e qualquer argumento extra da função vem como argumentos dentro do **...**
```
## function (X, FUN, ...) 
## {
##     FUN <- match.fun(FUN)
##     if (!is.vector(X) || is.object(X)) 
##         X <- as.list(X)
##     .Internal(lapply(X, FUN))
## }
## <bytecode: 0x7ff7a1951c00>
## <environment: namespace:base>
```
Exemplo com função anônima, comparando com sapply:
```
> x <- 1:5
> sapply(x, function(x){x + 1})
[1] 2 3 4 5 6
> lapply(x, function(x){x + 1})
[[1]]
[1] 2

[[2]]
[1] 3

[[3]]
[1] 4

[[4]]
[1] 5
> x <- list(a = 1:4, b = rnorm(10), c = rnorm(20, 1), d = rnorm(100, 5))
> lapply(x, mean)
$a
[1] 2.5

$b
[1] -0.2592703

$c
[1] 0.5095762

$d
[1] 4.979392
```
**runif(x)** gera x valores aleatórios, com argumentos de max e min.
```
> lapply(x, runif, min = 0, max = 10)
[[1]]
[1] 2.61743

[[2]]
[1] 9.726315 3.627900

[[3]]
[1] 7.986620 8.443881 8.321763

[[4]]
[1] 1.166017 7.193488 5.380282 5.942225
```
**Funções Anônimas**
```
> x <- list(a = matrix(1:4, 2, 2), b = matrix(1:6, 3, 2))
> x
$a
     [,1] [,2]
[1,]    1    3
[2,]    2    4

$b
     [,1] [,2]
[1,]    1    4
[2,]    2    5
[3,]    3    6

# Suponha que queremos pegar a primeira coluna de cada matriz

> lapply(x, function(z){z[,1]})
$a
[1] 1 2

$b
[1] 1 2 3
```

##### apply()

É usada para avaliar uma função nas margens de um arranjo. Tipicamente usada para aplicar funções a linhas ou colunas de matrizes. Pode ser usada com arranjos gerais, ex-- pegando a média de um arranjo de matrizes--. Não é muito mais rápido do que escrever um ciclo, porém funciona em uma linha.
```
>str(apply)
function (x, MARGIN, FUN, ...)
```
Decodificando o que vemos acima:
**x**: um arranjo

**MARGIN**: é um vetor de inteiros indicando quais margens deveriam ser retidas.

**FUN**: é a função sendo aplicada

**...**: argumentos extras.

Como podemos ver abaixo, criamos uma matriz 20x10. Dela mantemos a **segunda** dimensão, as **colunas**, e ignoramos a primeira dimensão, que sao as linhas. Assim aplicamos *mean()* às **10** colunas, obtendo a média de cada uma. Vamos utilizar a matriz no final da lição para os próximos exemplos.

```
> apply(x, 2, mean)
 [1]  0.18800750  0.05201392  0.37343831 -0.19715015 -0.33738285
 [6] -0.36289180  0.23275679 -0.07630139 -0.12231749 -0.41068884
```
Nesse segundo exemplo, focamos na **primeira** dimensão, as **linhas**, e obtemos a soma de cada uma.
```
> apply(x, 1, sum)
 [1] -3.4687016 -5.9377360 -1.0399752  1.0202298 -1.6055288 -1.1262478
 [7] -1.4424097 -0.2449632 -3.8460723 -1.1852833  2.7985345 -2.3378377
[13] -0.7571568  2.2833380  1.6554498 -0.9138204  3.8563300  4.6742666
[19] -6.1994674  0.6067315
```
Existem funções que são a otimização de algumas utilizações da função apply(). Elas são muito mais eficientes. São elas:

**rowSums()** = apply(x, 1, sum)

**colSums()** = apply(x, 2, sum)

**rowMeans()** = apply(x, 1, mean)

**colMeans()** = apply(x, 2, mean)

Outro exemplo de função que pode ser aplicado com apply() é o o **quantile()** para encontrar os quantis dentro de uma lista. Aplicamos o quantile() a cada linha. A função exige os argumentos de quais quantis queremos; buscamos 25% e 75%. 
```
> apply(x, 1, quantile, probs = c(0.25, 0.75))
          [,1]       [,2]        [,3]        [,4]       [,5]
25% -1.1974182 -0.8239562 -0.89770275 -0.45019192 -0.5281022
75%  0.1059192  0.1247921  0.08641744  0.09694716  0.6547386
          [,6]       [,7]       [,8]         [,9]      [,10]
25% -0.7469604 -0.7241985 -0.5948009 -0.769527213 -0.5832312
75%  0.3585018  0.3455060  0.9506084 -0.005505612  0.1372027
         [,11]      [,12]      [,13]       [,14]      [,15]
25% -0.1091304 -1.1470910 -0.7845137 -0.05103625 -0.7007251
75%  0.9659275  0.4870687  0.4970074  0.40292902  0.8272681
         [,16]      [,17]       [,18]      [,19]      [,20]
25% -0.8091430 -0.8354679 0.005535201 -1.2898949 -0.9695869
75%  0.7717053  1.1051728 0.787383773  0.2781535  0.8603504
```
Supomos que tenhamos um arranjo feito de 10 matrizes 2x2. Podemos cria uma aleatória usando **rnorm(x)** para gerar x observações. Arranjo utilizado no final da lição.

Nesse exemplo vamos pega a média para $$a_{1,1}$$,$$a_{1,2}$$,$$a_{2,1}$$,$$a_{2,2}$$ de todas as matrizes.
```
> my_array <- array(rnorm(2 * 2 * 10), c(2, 2, 10))
> apply(my_array, c(1, 2), mean)
           [,1]       [,2]
[1,] -0.2748534 -0.0659356
[2,] -0.3939356  0.3461228

# OU

> rowMeans(my_array, dims = 2)
           [,1]       [,2]
[1,] -0.2748534 -0.0659356
[2,] -0.3939356  0.3461228
```

> ARRANJO UTILIZADO

```
> my_array <- array(rnorm(2 * 2 * 10), c(2, 2, 10))
> my_array
, , 1

          [,1]         [,2]
[1,] -0.151632 -0.715428673
[2,]  2.133298  0.002634547

, , 2

           [,1]       [,2]
[1,] -1.8782373 -0.3709838
[2,] -0.9743144  1.5790925

, , 3

            [,1]       [,2]
[1,] -0.24016655 -1.3587181
[2,]  0.04668039  0.9943709

, , 4

            [,1]      [,2]
[1,]  0.05054523 0.1533727
[2,] -0.01341810 0.2313257

, , 5

           [,1]       [,2]
[1,] -0.6077648 -0.7734936
[2,] -1.5162868 -0.5885195

, , 6

           [,1]        [,2]
[1,] -0.8759329 -0.03510193
[2,] -0.8172949  0.60625592

, , 7

          [,1]       [,2]
[1,] 0.1746697  0.1709947
[2,] 0.7347790 -0.2693019

, , 8

           [,1]      [,2]
[1,] -0.8768544 1.0803543
[2,] -1.4186601 0.4048468

, , 9

           [,1]       [,2]
[1,] -0.4386305  0.1164227
[2,] -1.1963369 -0.9954588

, , 10

           [,1]     [,2]
[1,]  2.0954695 1.073226
[2,] -0.9178025 1.495981
```

> MATRIZ UTILIZADA

```
> x <- matrix(rnorm(200), 20, 10)
> x
            [,1]        [,2]       [,3]         [,4]        [,5]
 [1,] -1.0288320 -1.41648770  1.8037471 -1.607561656  0.74012835
 [2,] -0.8182733  0.23104672 -0.1939720  1.023998505 -2.60226140
 [3,]  1.4188046 -0.08097544 -0.7575889 -1.038093020 -0.21536550
 [4,]  2.2437526 -0.01616072 -0.1407965  1.178141340 -0.75243235
 [5,] -2.0785401  0.85021345  0.7986418 -0.887563620 -0.20128856
 [6,]  1.3934347  0.23348628 -0.5822791 -0.695607360 -0.76407808
 [7,] -1.2328586 -1.52170575  0.2140460  1.367529974 -0.76476670
 [8,]  1.3346220 -2.29978857 -0.3960134  0.195209004  0.39457576
 [9,] -0.9099239  0.14091012  0.7216804 -0.837428842 -0.44475282
[10,]  0.1711611  0.01692126 -0.6669633 -0.945317305  0.03532757
[11,]  1.4891085  1.25094221 -0.1337118 -0.599548970 -0.03538615
[12,]  0.5045798 -1.46844513  0.4345356 -1.264690273  0.01937725
[13,] -0.5583864  2.16848950  0.5232391 -1.560332762  0.41831260
[14,] -0.3278867 -1.04156125  0.3381398  1.455471971 -0.06903448
[15,] -0.3316311  0.17378418  0.8586924  1.125778544 -0.84882989
[16,]  0.8738627  0.39543150  1.1826307  0.465232943 -1.38290570
[17,]  1.1078743 -1.23894322  1.9576741  1.097068369 -0.42221293
[18,]  0.7878613  1.70454469  1.4756485  0.001868425  0.62612602
[19,] -0.7421125  0.80254336  0.5343091 -1.294552519 -1.27592223
[20,]  0.4635327  2.15603281 -0.5028936 -1.122605776  0.79773219
             [,6]        [,7]         [,8]        [,9]       [,10]
 [1,] -0.72303331 -1.25361362 -0.154891357  0.04592538  0.12591719
 [2,] -0.82585047 -0.81531552  0.287543352 -1.67547303 -0.54917893
 [3,] -1.03540979 -0.94440737  1.455949605  0.09427963  0.06283090
 [4,] -0.82480008  0.12775049  0.004537156 -0.29925934 -0.50050277
 [5,] -0.18614548 -0.55808014 -0.438168382  0.22302884  0.87237331
 [6,] -0.83660058  0.94765557  0.378736494  0.29779774 -1.49879351
 [7,] -0.22485702 -0.30560060 -0.602494075  1.23897101  0.38932602
 [8,] -1.52348853  1.51487281  1.135952668 -0.66106347  0.06015849
 [9,]  0.50240431 -0.46719951 -0.565822326 -0.53810558 -1.44783423
[10,] -0.33203500  1.49665777  0.901615519 -0.22721351 -1.63543753
[11,]  0.98366862  0.52993922  0.912704193 -1.79997080  0.20078946
[12,]  0.77673322  1.42466179 -1.573214383 -0.79429316 -0.39708237
[13,]  0.01876993 -0.85988947 -1.252342407  0.71146153 -0.36647839
[14,]  0.32597790  0.05809249  0.002958453  1.11665437  0.42452543
[15,]  0.29975642  1.44991458 -0.823756450  0.73299525 -0.98125415
[16,] -0.57245561 -0.88803873 -0.384605610  0.89915899 -1.50213167
[17,]  1.02451782  1.78956473  0.739653288 -1.22564688 -0.97321958
[18,] -0.29515258 -0.60036352  0.171247136  0.01653553  0.78595104
[19,] -1.84108897  0.40040099 -1.211100447 -1.48335528 -0.08858896
[20,] -1.96874679  1.60813383 -0.510530297  0.88122310 -1.19514663
```

##### mapply()

É uma versão multivariada de **apply()** que aplica uma função num conjunto de argumentos de form paralela.
```
> str(mapply)
function (FUN, ..., MoreArgs = NULL, SIMPLIFY = TRUE, 
    USE.NAMES = TRUE) 
```
>**FUN**: função a ser aplicada
>
>**...**: argumemntos
>
>**MoreArgs**: lista de outros argumemntos em FUN
>
>**SIMPLIFY**: indica se o resultado deve vir simplificado

**lapply(x)** aplica função a uma lista x, mas e se tiver duas listas, cada um necessitando argumentos diferentes de uma determinada função? Aqui que entra **mapply()**.

Exemplo de uso. A função abaixo é idêntica a list(rep(1, 4), rep(2, 3), rep(3, 2), rep(4, 1)):
```
> mapply(rep, 1:4, 4:1)
[[1]]
[1] 1 1 1 1

[[2]]
[1] 2 2 2

[[3]]
[1] 3 3

[[4]]
[1] 4
```
Outro exemplo:
```
> noise <- function(n, mean, sd) {
+     rnorm(n, mean, sd)
+ }
> noise(5, 1, 2)
[1] 3.2375728 2.0660008 0.3015511 1.3750976 1.6583198
```
Como faz para inserir valores de vetores numa função que não aceita vetores? Geralmente usa-se um ciclo *for*, porém *mapply()* facilita as nossas vidas.
```
> mapply(noise, 1:5, 1:5, 2)
[[1]]
[1] 1.182528

[[2]]
[1] 2.270017 1.857737

[[3]]
[1] 3.026373 4.406742 4.533147

[[4]]
[1] 0.8356212 3.6223115 7.4120700 5.2022007

[[5]]
[1] 5.231018 4.661119 2.909495 4.854264 8.297683
```

##### tapply()

Aplicar funções em subconjuntos de vetores. Geralmente é necessário definir primeiro quais elementos do grupo pertencem ao subconjunto antes de aplicar uma função e para cada grupo será calculado algo.
```
> str(tapply)
function (X, INDEX, FUN = NULL, ..., default = NA, 
    simplify = TRUE)  
```
> **x**: é um vetor
>
>**INDEX**: é um fator ou lista de fatores
>
>**FUN**: é a função
>
>**...**: contem os argumemntos para FUN
>
>**simplify**: simplifica o resultado

Exemplo:
```
> zed <- c(rnorm(10), runif(10), rnorm(10, 1))
> f <- gl(3, 10) # cria 3 grupos de tamanho 10 cada
> f
 [1] 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3
Levels: 1 2 3
> tapply(zed, f, mean)
         1          2          3 
-0.3145874  0.4344597  1.4299882 
> tapply(zed, f, range)
$`1`
[1] -1.1796714  0.8109692

$`2`
[1] 0.06941466 0.95021127

$`3`
[1] 0.3000944 2.8496935
```

##### split()

Pega um objeto ou vetor e a divide em grupos determinados por fatores ou lista de fatores, aplica a função e junta os grupos num pedaço só novamente. É muito útil sendo aplicado junto a funções de ciclo como *lapply()* e *sapply()*. Ela sempre devolde uma lista.
```
> str(split)
function (x, f, drop = FALSE, ...)
```
**x** é o vetor (ou lista) or data frame

**f** é o fator (ou será forçado a um fator) ou lista de fatores.

**drop** indica que níveis vazios de fatores são ignorados.

```
# Usando a variável zed anterior
# "zed <- c(rnorm(10), runif(10), rnorm(10, 1))"
> split(zed, f)
$`1`
 [1] -0.79036976 -0.09239610 -1.17967137  0.03002006 -1.02713486
 [6]  0.44073627  0.81096919 -0.15611145 -0.75300812 -0.42890738

$`2`
 [1] 0.51809321 0.30123497 0.30230853 0.95021127 0.29987675
 [6] 0.06941466 0.10863322 0.08789710 0.87654851 0.83037923

$`3`
 [1] 2.8496935 1.4152770 1.8167129 1.0660863 1.1594433 0.5268611
 [7] 1.6234265 1.4716132 0.3000944 2.0706741
```
Exemplo de usar split() em conjunto com lapply(). A função do exemplo é melhor com tapply() por ser mais compacto escrever.
```
> lapply(split(zed, f), mean)
$`1`
[1] -0.3145874

$`2`
[1] 0.4344597

$`3`
[1] 1.429988
```
Split pode ser utilizado para coisas muito mais complicadas. Vamos puxar os dados de qualidade de ar do curso "hw1_data.csv".
```
> library(datasets)
> head(airquality)
  Ozone Solar.R Wind Temp Month Day
1    41     190  7.4   67     5   1
2    36     118  8.0   72     5   2
3    12     149 12.6   74     5   3
4    18     313 11.5   62     5   4
5    NA      NA 14.3   56     5   5
6    28      NA 14.9   66     5   6
```
Podemos usar uma das colunas como os fatores, separar os dados pelos fatores, e aplicar uma função a determinadas colunas,
```
> a <- split(airquality, airquality$Month)
> lapply(a,function(x){colMeans(x[,c("Ozone", "Solar.R", "Wind")])})
$`5`
   Ozone  Solar.R     Wind 
      NA       NA 11.62258 

$`6`
    Ozone   Solar.R      Wind 
       NA 190.16667  10.26667 

$`7`
     Ozone    Solar.R       Wind 
        NA 216.483871   8.941935 

$`8`
   Ozone  Solar.R     Wind 
      NA       NA 8.793548 

$`9`
   Ozone  Solar.R     Wind 
      NA 167.4333  10.1800 

```
**sapply()** faria a mesma coisa porém mudando o formato pra uma matriz.
```
> sapply(a,function(x){colMeans(x[,c("Ozone", "Solar.R", "Wind")])})
               5         6          7        8        9
Ozone         NA        NA         NA       NA       NA
Solar.R       NA 190.16667 216.483871       NA 167.4333
Wind    11.62258  10.26667   8.941935 8.793548  10.1800
```
É possível colocar um argumento para remover valores *NA*, **na.rm = TRUE**, que remove os valores *NA* antes de calcular as médias.
```
> sapply(a,function(x){colMeans(x[,c("Ozone", "Solar.R", "Wind")], na.rm =TRUE)})
                5         6          7          8         9
Ozone    23.61538  29.44444  59.115385  59.961538  31.44828
Solar.R 181.29630 190.16667 216.483871 171.857143 167.43333
Wind     11.62258  10.26667   8.941935   8.793548  10.18000
```
Suponha que nos dados os valores comtêm mais de um fator, podendo ser, por exemplo, faixa etária e sexo. E gostaríamos de ver as combinações dos niveis dentre os fatores. Vamos simular isso. **gl(n,f)** gera n quantidade de f fatores e **interaction()** combina tais fatores. Ao colocar f1 aplicado a zed, obtemos y e com f2 a zed obtemos y2. usar f1 e f2 seria usar a intercessão de f1 com f2.
```
# sexo
> f1 <- gl(2, 5)
> f1
 [1] 1 1 1 1 1 2 2 2 2 2
Levels: 1 2
# faixa etária
> f2 <- gl(5, 2)
> f2
 [1] 1 1 2 2 3 3 4 4 5 5
Levels: 1 2 3 4 5
> interaction(f1, f2)
 [1] 1.1 1.1 1.2 1.2 1.3 2.3 2.4 2.4 2.5 2.5
Levels: 1.1 2.1 1.2 2.2 1.3 2.3 1.4 2.4 1.5 2.5
> str(split(zed, list(f1, f2)))
List of 10
 $ 1.1: num [1:6] -0.7904 -0.0924 0.5181 0.3012 2.8497 ...
 $ 2.1: num(0) 
 $ 1.2: num [1:6] -1.18 0.03 0.302 0.95 1.817 ...
 $ 2.2: num(0) 
 $ 1.3: num [1:3] -1.03 0.3 1.16
 $ 2.3: num [1:3] 0.4407 0.0694 0.5269
 $ 1.4: num(0) 
 $ 2.4: num [1:6] 0.811 -0.1561 0.1086 0.0879 1.6234 ...
 $ 1.5: num(0) 
 $ 2.5: num [1:6] -0.753 -0.429 0.877 0.83 0.3 ...
```
O argumento **drop = TRUE** retira níveis vazios
```
> str(split(zed, list(f1, f2), drop = TRUE))
List of 6
 $ 1.1: num [1:6] -0.7904 -0.0924 0.5181 0.3012 2.8497 ...
 $ 1.2: num [1:6] -1.18 0.03 0.302 0.95 1.817 ...
 $ 1.3: num [1:3] -1.03 0.3 1.16
 $ 2.3: num [1:3] 0.4407 0.0694 0.5269
 $ 2.4: num [1:6] 0.811 -0.1561 0.1086 0.0879 1.6234 ...
 $ 2.5: num [1:6] -0.753 -0.429 0.877 0.83 0.3 ...
```

> zed
```
> zed
 [1] -0.79036976 -0.09239610 -1.17967137  0.03002006
 [5] -1.02713486  0.44073627  0.81096919 -0.15611145
 [9] -0.75300812 -0.42890738  0.51809321  0.30123497
[13]  0.30230853  0.95021127  0.29987675  0.06941466
[17]  0.10863322  0.08789710  0.87654851  0.83037923
[21]  2.84969350  1.41527703  1.81671292  1.06608626
[25]  1.15944328  0.52686111  1.62342647  1.47161321
[29]  0.30009436  2.07067409
```

#### Debugging Tools - Diagnosing the Problem

Um **bug** literalmente é um inseto. Antigamente os computadores eram enormes e tinha vez que algum inseto entrava e atrapalhava o seu funcionamento. O prefixo inglês *de* significa tirar, ou retornar a um estado sem; no caso de **Debug**, significa tirar um bug, ou insento do computador. Atualmente computadores comerciais são menores, porém o linguajar continuou para quando existe algum problema no funcionamento de um programa, o *bug* sendo a fonte do problema.

Vamos falar abaixo sobre ferramentas que são boas para descobrir o que deu errado com um problema depois do erro ter acontecido. 

Existem três tipos principais de indicações de erro:

**message**: Ou mensagem, ma notificação/diagnóstico genérica de que algo deu errado, produzido pela função *message*; a execução da função continua. Acontece no meio da execução.

**warning**: Ou aviso, uma indicação de que algo deu errado, mas não é necessariamente fatal; a execução da função continua; é gerada pela função *warning*. Aparece no final da execução.

**error**: uOu erro, uma indicação de que um problema fatal ocorreu; a execução para; é produzido pela função **stop**.

**condition**: Ou condição, é um conceito genérico de alto nível indicando que algo inesperado poderá ocorrer; todas essas funções anteriores são condições; programadores podem criar suas próprias condições.

-----------------

Exemplo, tomamos um log de um número negativo
```
> log(-1)
[1] NaN
Warning message:
In log(-1) : NaNs produced
```
Vemos que depois da execução temos um warning indicando que quando tentamos tirar o log de -1, NaNs são produzidos, lembrando que NaN significa "Não um Número".

Tem vez que isso é OK, pois pode ocorrer de num cálculo realmente aparecer um número negativo. Você não vai querer que a execução pare devido isso, mas é bom saber que algo assim foi tentado, por isso o *warning*.

Tem vez que numa função, queremos fazer determinada coisa porém a última coisa na função é uma variável que não queremos que seja imprimida, porém, além de devolver determinada variável, R imprime sempre a última coisa de uma função. Para isso não ocorrer usamos a função **invisible(x)** que impede x de ser impresso, porém continua devolvendo x.

Uma função que contem isso é **load()** que retorna um vetor de caracteres contendo os nomes dos objetos que são carregados, porém não os imprime, devido a função retornar invisívelmente.

Em relação ao exemplo abaixo, toda função **print()** retorna a **string** (linha de texto) que ela imprime. Então quando usa print(x), ela retorna a *string* x, mas não vemos isso pois o valor de retorno é invisível utilizando a função *invisible()*.

O retorno de printmessage() abaixo é seu argumemnto, 1.
```
> printmessage <- function(x){
     if(x > 0){
         print("x é maior do que zero")
     } else{
         print("x é menor ou igual a zero")
     }
     invisible(x)
}
> printmessage(1)
[1] "x é maior do que zero"
> retorno <- printmessage(1)
[1] "x é maior do que zero"
> retorno
[1] 1
> printmessage(NA)
Error in if (x > 0) { : missing value where TRUE/FALSE needed
```
Ao tentar imprimir algo que não é um número, o programa dar erro e para. Depois mostra aonde ocorreu o erro e mostra o que era necessário ocorrer; nesse caso o programa procurou por um argumento verdadeiro ou falso e não obteve nemhum dos dois.

Podemos resolver esse problema criando uma condição para NA. Lembrando que colocamos o *else if*, para que o que era um segundo *if* não rodar (e não aparecer o erro anterior). 
```
> printmessage <- function(x){
     if(is.na(x)){
         print("x is a missing value!")
     }
     else if(x > 0){
         print("x é maior do que zero")
     } else{
         print("x é menor ou igual a zero")
     }
     invisible(x)
}
> printmessage(NA)
[1] "x is a missing value!"
```
Assim ao rodar o seguinte algoritmo, ele completa toda a execução.
```
> meu_log <- log(-1)
Warning message:
In log(-1) : NaNs produced
> printmessage(meu_log)
[1] "x is a missing value!"
```

Algumas perguntas que você deveria se perguntar para localizar, além de tudo, se o problema está no programa ou no usuário:
 * Qual era sua entrada? Como chamou a função?
 * O que estava esperando? Saída, mensagens ou outros resultados?
 * O que obteve?
 * Como que o que obteve difere do que esperava?
 * Suas expectativas fazem sentido?
 * Consegue reproduzir tal problema exatamente?
   * Alguns problemas ocorrem para entrada específicas. Por exemplo, se estiver usando um gerador de números aleatórios, é bom estabelecer um **seed** (semente). Uma semente é um número aplicado a um gerador de números aleatórios, e tal gerador sempre vai gerar um mesmo resultado para cada determinada seed. Isso facilita na reprodução do problema. A dificuldade de reprodução é determinada pelos elementos fora do seu controle.

##### Debugging Tools - Basic Tools

Existem cinco ferramentas básicas (e algumas extras) que R fornece para ajudar no conserto do programa. Existem pessoas que passam anos sem saber da existência delas, programando bem, mas, apesar disso, é sempre bom terem elas em mãos.

**traceback()**: imprime o **call stack** da função depois que o erro occore. O *call stack* seria a sequência de objetos rodados no algoritmo. Essa função não retorna algo caso não haja erro.

**debug()**: **flags**, ou seja marca uma função, para o modo *debug*, que nos permite passar por uma função uma linha por vez, sempre que ela for chamada.

**browser()**: suspend a execução de uma função, em qualquer parte da função, toda vez que for chamada e coloca ela em modo debug.

**trace()**: permite inserir um codigo de **debugging** (gerúndio de debug) numa função em locais específicos (como a função *browser*).

**recover()**: ou recuperar, permite modificar o comportamento do erro para que possa visualizar o *call stack*. 

Outra coisa que poderá fazer é colocar um monte de **print()** e **cat()** dentro das funções.

##### Debugging Tools - Using the Tools

###### traceback()
Utiliza-se traceback para encontrar onde ocorreu o erro no algoritmo. O *traceback()* tem que ser chamado imediatamente após o erro ocorrer. É muito útil enviar o *traceback()* para alguém que esteja ajudando com o debug do código.
```
> mean(u)
Error in mean(u) : object 'u' not found
> traceback()
1: mean(u)
```
###### debug()
O **Browser**, ou visualizador, mostra o ambiente do debug, que é o próprio código da função sendo debugged (verbo passado de debug). 

O *debug* pode ser usado em qualquer função, independente se ela já existe ou você criou. Primeiro inserimos no debug a função que queremos visualizar o erro, quando ocorrer. Ao utilizar a função com debug, ela imprime seu código e depois podemos visualizar linha por linha o seu funcionamento. É possível colocar funções num *debug()* dentro da função em *debug()*, fazendo ela ser debugged quando for chamada dentro do Browser.
```
> debug(lm)
> lm(mean(x) - u)
debugging in: lm(mean(x) - u)
debug: {
    ret.x <- x
    ret.y <- y
    cl <- match.call()
    mf <- match.call(expand.dots = FALSE)
    m <- match(c("formula", "data", "subset", "weights", "na.action", 
        "offset"), names(mf), 0L)
    mf <- mf[c(1L, m)]
    mf$drop.unused.levels <- TRUE
    mf[[1L]] <- quote(stats::model.frame)
    mf <- eval(mf, parent.frame())
    if (method == "model.frame") 
        return(mf)
    else if (method != "qr") 
        warning(gettextf("method = '%s' is not supported. Using 'qr'", 
            method), domain = NA)
    mt <- attr(mf, "terms")
    y <- model.response(mf, "numeric")
    w <- as.vector(model.weights(mf))
    if (!is.null(w) && !is.numeric(w)) 
        stop("'weights' must be a numeric vector")
    offset <- as.vector(model.offset(mf))
    if (!is.null(offset)) {
        if (length(offset) != NROW(y)) 
            stop(gettextf("number of offsets is %d, should equal %d (number of observations)", 
                length(offset), NROW(y)), domain = NA)
    }
    if (is.empty.model(mt)) {
        x <- NULL
        z <- list(coefficients = if (is.matrix(y)) matrix(NA_real_, 
            0, ncol(y)) else numeric(), residuals = y, fitted.values = 0 * 
            y, weights = w, rank = 0L, df.residual = if (!is.null(w)) sum(w != 
            0) else if (is.matrix(y)) nrow(y) else length(y))
        if (!is.null(offset)) {
            z$fitted.values <- offset
            z$residuals <- y - offset
        }
    }
    else {
        x <- model.matrix(mt, mf, contrasts)
        z <- if (is.null(w)) 
            lm.fit(x, y, offset = offset, singular.ok = singular.ok, 
                ...)
        else lm.wfit(x, y, w, offset = offset, singular.ok = singular.ok, 
            ...)
    }
    class(z) <- c(if (is.matrix(y)) "mlm", "lm")
    z$na.action <- attr(mf, "na.action")
    z$offset <- offset
    z$contrasts <- attr(x, "contrasts")
    z$xlevels <- .getXlevels(mt, mf)
    z$call <- cl
    z$terms <- mt
    if (model) 
        z$model <- mf
    if (ret.x) 
        z$x <- x
    if (ret.y) 
        z$y <- y
    if (!qr) 
        z$qr <- NULL
    z
}
Browse[2]>  
Browse[2]> 
debug: ret.x <- x
Browse[2]> 
debug: ret.y <- y
Browse[2]> 
debug: cl <- match.call()
Browse[2]> 
debug: mf <- match.call(expand.dots = FALSE)
Browse[2]> 
debug: m <- match(c("formula", "data", "subset", "weights", "na.action", 
    "offset"), names(mf), 0L)
Browse[2]> 
debug: mf <- mf[c(1L, m)]
Browse[2]> 
debug: mf$drop.unused.levels <- TRUE
Browse[2]> 
debug: mf[[1L]] <- quote(stats::model.frame)
Browse[2]> 
debug: mf <- eval(mf, parent.frame())
Browse[2]> 
Error in stats::model.frame(formula = mean(x) - u, drop.unused.levels = TRUE) : 
  object 'u' not found
```

###### recover()
É possível alterar o comportamento do error com `options(error = recover)`, alterando a opção global para a sessão de utilização de R atual.

Quando ocorrer um erro, ao invés do erro ser impresso e voltar-mos para o console, aparece um menu que é o *function call stack*, ou ordem de chamada dentro da função, que é (a call stack) a mesma coisa que obteria chamando um *traceback()* depois de um erro.
```
> read.csv("arquivoquenãoexiste")
Error in file(file, "rt") : cannot open the connection
In addition: Warning message:
In file(file, "rt") :
  cannot open file 'arquivoquenãoexiste': No such file or directory

Enter a frame number, or 0 to exit   

1: read.csv("arquivoquenãoexiste")
2: read.table(file = file, header = header, sep = sep, quote = quote, dec =
3: file(file, "rt")

Selection:
```
No selection poderá selecionar, nesse caso, 1, 2 ou 3 e browse (visualizar) o cógido.