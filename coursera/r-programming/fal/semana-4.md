# Anotações Fal

## R Programming

### Semana 4 - Simulation and Profiling

Essa semana sobre como simular dados em R. Também sera coberto um perfilador que permite coletar informação detalhada de funções no R que estão rodando para identificar pontos de sobrecarga. O perfilador é uma ferramenta chave para otimizar programas. Também seŕa coberto a função **str**, uma das mais importantes no R.

Os Objetivos de aprendizagem para essa semana são:
 * Chamar a função `str()` num objeto arbitrário no R;
 * Descrever a diferença entre as saídas `by.self` e `by.total` produzidas pelo perfilador;
 * Simular uma variável aleatória normal com uma média e desvio padrão arbitrários e;
 *Simular dados de um modelo linear normal.
 
#### The str Function

**str()** é uma ferramenta de diagnóstico alternativa ao `summary()`. É especialmente adequada para mostrar conteúdo de listas (possívelmente **nested**, aninhada em vários níveis) de forma abreviada. Geralmente é uma linha por objeto básico.

Aplicada a uma função ela mostra os argumentos básicos:
```
> str(ls)
function (name, pos = -1L, envir = as.environment(pos), all.names = FALSE, 
    pattern, sorted = TRUE)  
```
Aplicada a um vetor, mostra informações básicas.
```
> x <- rnorm(100, 2, 4)
> str(x)
 num [1:100] -4.26 2.6 3.82 5.16 6.34 ...
> # Dieferente do summary, que mostra mais detalhes. 
> summary(x)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
 -7.082  -0.738   1.512   1.505   3.768  11.689 
```
Para fatores
```
> f <- gl(40, 10)
> str(f)
 Factor w/ 40 levels "1","2","3","4",..: 1 1 1 1 1 1 1 1 1 1 ...
> summary(f)
 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 
26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 
```
Para sets de dados para cada váriável tem um pouco de informação.
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
> str(airquality)
'data.frame':	153 obs. of  6 variables:
 $ Ozone  : int  41 36 12 18 NA 28 23 19 8 NA ...
 $ Solar.R: int  190 118 149 313 NA NA 299 99 19 194 ...
 $ Wind   : num  7.4 8 12.6 11.5 14.3 14.9 8.6 13.8 20.1 8.6 ...
 $ Temp   : int  67 72 74 62 56 66 65 59 61 69 ...
 $ Month  : int  5 5 5 5 5 5 5 5 5 5 ...
 $ Day    : int  1 2 3 4 5 6 7 8 9 10 ...
```
Para matrizes
```
> m <- matrix(rnorm(100), 10, 10)
> str(m)
 num [1:10, 1:10] 0.373 -0.404 0.783 0.147 0.172 ...
```
Para listas aninhadas (copiei apenas os primeiros 2 meses para não ficar feio o exemplo abaixo)
```
> s <- split(airquality, airquality$Month)
> str(s)
List of 5
 $ 5:'data.frame':	31 obs. of  6 variables:
  ..$ Ozone  : int [1:31] 41 36 12 18 NA 28 23 19 8 NA ...
  ..$ Solar.R: int [1:31] 190 118 149 313 NA NA 299 99 19 194 ...
  ..$ Wind   : num [1:31] 7.4 8 12.6 11.5 14.3 14.9 8.6 13.8 20.1 8.6 ...
  ..$ Temp   : int [1:31] 67 72 74 62 56 66 65 59 61 69 ...
  ..$ Month  : int [1:31] 5 5 5 5 5 5 5 5 5 5 ...
  ..$ Day    : int [1:31] 1 2 3 4 5 6 7 8 9 10 ...
 $ 6:'data.frame':	30 obs. of  6 variables:
  ..$ Ozone  : int [1:30] NA NA NA NA NA NA 29 NA 71 39 ...
  ..$ Solar.R: int [1:30] 286 287 242 186 220 264 127 273 291 323 ...
  ..$ Wind   : num [1:30] 8.6 9.7 16.1 9.2 8.6 14.3 9.7 6.9 13.8 11.5 ...
  ..$ Temp   : int [1:30] 78 74 67 84 85 79 82 87 90 87 ...
  ..$ Month  : int [1:30] 6 6 6 6 6 6 6 6 6 6 ...
  ..$ Day    : int [1:30] 1 2 3 4 5 6 7 8 9 10 ...
```

#### Simulation - Generating Random Numbers

Simulações são muito importante para estatística e várias outras aplicações em R.

**rnorm()**: gera um número aleatório que varia para a média e desvio padrão indicado.

**dnorm()**: avalia a densidade de propabilidade normal (para a média/desvio padrão indicado) para um ponto (ou vetor de pontos).

**pnorm()**: avalia a função distribuição acumulada para uma distribuição normal.

**rpois()**: gera um Poisson aleatório que varia com a taxa indicada.

Funções de distribuição de probabilidades geralmente tem quatro funções associadas. Tais funções são prefixadas com um

 * **d** para **densidade**;
 * **r** para **gerar número aleatório** *(random)*;
 * **p** para **distribuição acumulada**;
 * **q** para **função quantílica**.

Então para uma distribuição gama, ou poisson teríamos dgama ou dpois, por exemplo.
```
> ppois(4, 2) ## Distribuição acumulativa
[1] 0.947347 ## Pr(x <= 2) se a taxa é 4
```

Os comandos sempre pedem uma média e um desvio padrão. Caso não seja especificado, a média é zero e o desvio padrão é 1.
```
dnorm(x, mean = 0, sd = 1, log = FALSE)
# A maior parte das vezes vai querer usar o log da função de densidade
# mas o valor default aqui é Falso.

pnorm(q, mean = 0, sd = 1, lower.tail = TRUE, log.p = FALSE)
qnorm(p, mean = 0, sd = 1, lower.tail = TRUE, log.p = FALSE)
# Para as duas anteriores o lower.tail é a cauda esquerda das funções
# caso queira avaliar o lado direito deixe esse valor como Falso.

rnorm(n, mean = 0, sd = 1)
n aqui significa a quantidade de obserações que queira gerar.

se pnorm(z) = Φ(z), qnorm(z) = Φ⁻¹(z)
```

Estabelecer um **seed** ou semente é muito importante para reprodutibilidade. Para cada determinada semente estabelecida, uma função geradora de números aleatórios sempre apresentará a mesma sequência em seus resultados. Estabelecemos uma semente com `set.seed(n)` n sendo um número inteiro que servirá de semente. 

#### Simulation - Simulating a Linear Model

Como podemos simular dados de um modelo, como um modelo linear?
Vamos usar com exemplo o modelo proposto abaixo.

$$y = β_{0}+β_{1}x+ε$$

onde ε~ℕ(0, 2²). Assumimos que x~ℕ(0, 1²), $β_{0}=0.5$ e $β_{1}=2$
```
> set.seed(20)
> x <- rnorm(100)
> # Ou podemos usar uma distribuição binomial para x
> # x <- rbinom(100, 1, 0.5)
> e <- rnorm(100, 0, 2)
> y <- 0.5 + 2 * x + e
> summary(y)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
-6.4084 -1.5402  0.6789  0.6893  2.9303  6.5052 
> plot(x, y)
```
Nota-se que ao alterar **x**, **y** é automaticamente alterado também. Todavia para atualizar y quando altera-se a semente de **x**, é importante definir o **y** e o **e** de novo após a inserção da nova semente.

Suponhamos que precisamos modelar algo que resulta em valores discretos, ou seja não contínuos. Isso levaria a uma distribuição dos erros diferente da normal.

Então vamos tentar algo um pouco mais complicado generalizando o modelo com um modelo Poisson onde Y~Poisson(μ)
$$log(μ) = β_{0}+β_{1}x$$
e $β_{0}=0.5$ e $β_{1}=0.3$. Precisamos da funnção `rpois` para isso
```
set.seed(1)
> x <- rnorm(100)
> log.mu <- 0.5 + 0.3 * x
> y <- rpois(100, exp(log.mu)) # Para obter a média é necessário exponenciar a variável
> summary(y)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   0.00    1.00    1.00    1.55    2.00    6.00 
> plot(x, y)
```




