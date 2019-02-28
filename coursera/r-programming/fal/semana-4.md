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

**r***norm()*: gera um número aleatório que varia para a média e desvio padrão indicado.

**d***norm()*: avalia a densidade de propabilidade normal (para a média/desvio padrão indicado) para um ponto (ou vetor de pontos).

**p***norm()*: avalia a função distribuição acumulada para uma distribuição normal.

**r***pois()*: gera um Poisson aleatório que varia com a taxa indicada.

Funções de distribuição de probabilidades, como as descritas acima, geralmente tem quatro funções associadas. Tais funções são **prefixadas** com um

 * **d** para **densidade**;
 * **r** para **gerar número aleatório** *(random)*;
 * **p** para **distribuição acumulada**;
 * **q** para **função quantílica**.

Então para uma distribuição *gama*, ou *poisson* teríamos **d***gama()* ou **d***pois()*, por exemplo.
```
> ppois(4, 2) ## Distribuição acumulativa
[1] 0.947347 ## Pr(x <= 2) se a taxa é 4
```
No final da aula temos uma tabela com todas as distribuições que vem junto com R.

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

É importante notar também que a sequência de funções utilizadas também afeta os valores que saem, porém usar a mesma sequência para uma mesma semente gera os mesmos valores.
```
> # testando sequência de funções
> set.seed(1)  
> rnorm(3)
[1] -0.6264538  0.1836433 -0.8356286
> rnorm(3)
[1]  1.5952808  0.3295078 -0.8204684
> rnorm(4)
[1]  0.4874291  0.7383247  0.5757814 -0.3053884

> # testando a mesma sequência de funções
> set.seed(1)
> rnorm(3)
[1] -0.6264538  0.1836433 -0.8356286
> rnorm(3)
[1]  1.5952808  0.3295078 -0.8204684
> rnorm(4)
[1]  0.4874291  0.7383247  0.5757814 -0.3053884

# testando sequência de funções diferente
> set.seed(1)
> rnorm(3)
[1] -0.6264538  0.1836433 -0.8356286
> rnorm(4)
[1]  1.5952808  0.3295078 -0.8204684  0.4874291
> rnorm(3)
[1]  0.7383247  0.5757814 -0.3053884
```

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

#### Simulation - Random Sampling

**sample()** tira uma amostra de um conjunto de objetos escalares. Ela toma uma população **x**, e tira aleatoriamente uma amostra de tamanho **size**.
```
> str(sample)
function (x, size, replace = FALSE, prob = NULL)
```
Caso não seja colocado um tamaho, `sample()` devolverá uma permutação da população. Para uma **amostragem com reposição** o argumento **replace** deve ser **TRUE**, alternativamente uma amostragem por acaso único é o default de *replace = FALSE*.

Ao estabelecer uma semente, podemos obter a mesma amostragem de uma população.
```
> set.seed(1)
> sample(1:10, 4)
[1] 3 4 5 7
> sample(1:10, 4)
[1] 3 9 8 5
> sample(letters, 5)
[1] "q" "b" "e" "x" "p"
> sample(1:10)
 [1]  4  7 10  6  9  2  8  3  1  5
> sample(1:10)
 [1]  2  3  4  1  9  5 10  8  6  7
> sample(1:10, replace = TRUE)
 [1] 2 9 7 8 2 8 5 9 7 8
```
|Distribuições   |  Funções  |
|---|---|---|---|---|
| Amplitude Estudentizada  | ptukey  | qtukey  | dtukey  | rtukey  |
| Beta  | pbeta  | qbeta  | dbeta  | rbeta  |
| Binomial  | pbinom  |  qbinom | dbinom  | rbinom  |
| Binomial Negativo   | pnbinom  | qnbinom  | dnbinom  | rnbinom  |
| Cauchy  | pcauchy  | qcauchy  | dcauchy  | rcauchy  |
| Chi-Quadrado  | pchisq  | qchisq  | dchisq  | rchisq  |
| Exponencial  | pexp  | qexp  | dexp  | rexp  |
| F  | pf  | qf  | df  | rf  |
| Gamma  | pgamma  | qgamma  | dgamma  | rgamma  |
| Geometrica  | pgeom  | qgeom  | dgeom  | rgeom  |
| Hipergeometrica  | phyper  | qhyper  | dhyper  | rhyper  |
| Logistica  | plogis  | qlogis  | dlogis  | rlogis  |
| Log Normal  | plnorm  | qlnorm  | dlnorm  | rlnorm  |
| Normal  | pnorm  | qnorm  | dnorm  | rnorm  |
| Poisson  | ppois  | qpois  | dpois  | rpois  |
| t Student  | pt  | qt  | dt  | rt  |
| Uniforme  | punif  | qunif  | dunif  | runif  |
| Weibull  | pweibull  | qweibull  | dweibull  | rweibull  | 
| Estatística Soma dos Postos de Wilcoxon  | pwilcox  | qwilcox  | dwilcox  | rwilcox  |
| Estatística dos Postos Sinalizados de Wilcoxon  | psignrank  | qsignrank  | dsignrank  | rsignrank  |	  	 	 	 	
|[Tabela como tradução livre dessa Fonte](http://www.stat.umn.edu/geyer/old/5101/rlook.html)|

#### R Profiler (part 1)

O perfilador é bom para quando trabalha com dados ou algoritmos grandes. O perfilador é uma forma sistemática de examinar o tempo gasto em partes diferentes de um programa. É bom para fazer tudo funcionar no tempo certo e otimizar o software. Tem vez queu um programa funciona bem uma vez porém não quando iterado 1000 vezes.

Primeiro vem a pergunta mais importante **O meu código está muito lento?**.

A otimização do seu programa não deve ser feita na criação do programa, não é algo que deveria ter em mente quando escrevendo o código. A coisa mais importante nesse passo é examinar como fazer o código rodar o melhor possível para obter os resultados que quer e ser legível para outras pessoas. 

> "97% das vezes, otimização prematura é a fonte de todo mal" ~Donald Knuth

Depois de terminar a criação do programa, precisamos de obter dados para analisar o programa e detectar fontes de ineficiência: perfilando.

##### Usando system.time()

A primeira ferramenta que destacaremos não é o perfilador e sim o **system.time()**. Ela toma uma expressão, independente do tamanho, como entrada e devolve a quantidade de tempo (em **segundos**) que durou para avaliar dada expressão. Se ocorrer algum **erro**, ela devolve o tempo que leva até o erro ocorrer.

A **classe** do objeto retornado é **proc_time**. Tem duas noções importantes de tempo que devemos levar em consideração ao executar uma expressão:
 * **user time**: ou *tempo do usuário*, é o tempo de processo do(s) CPU(s) para a expressão, ou seja o tempo "sentido" pela máquina;
 * **elapsed time**: ou *tempo decorrido*, "tempo do relógio da parede"", é o tempo nós sentimos passar.
 
Geralmente o *user time* e o *elapsed time* são relativamente próximos. 
 * *elapsed time* pode vir a ser **maior** do que *user time* quando o CPU passa muito tempo sem fazer algo, apenas esperando.
 * *elapsed time* pode vir a ser **menor** do que *user time* se o computador estiver usando mais de um CPU para o processamento. R em si não faz isso (na época da gravação da aula), mas muitas bibliotecas como algumas de regressão fazem uso de mais de um CPU
   * Tais bibliotecas são chamadass de **multi-threaded BLAS libraries** ou bibliotecas com múltiplas linhas de encadeamento de execução SALB (Subprogramas de Algebra Linear Básica) que incluem vecLib/Accelerate (Mac), ATLAS (geral), ACML (AMD) e MKL (Intel);
   * Também existe o pacote **parallel** para computação paralela com múltiplos CPUs ou múltiplas máquinas.
```
> ## elapsed time > user time
> ## A maior parte do tempo é gasto esperando a rede conectar por isso que o tempo do sistema (0.004) de rodar apenas a função readLines é pequena. 
> system.time(readLines("http://www.jhsph.edu"))
   user  system elapsed 
  0.049   0.004   3.453 
  
> ## elapsed time < usere time
> ## Uma função para criar uma matriz hilbert
hilbert <- function(n){
        i <- 1:n
        1 / outer(i - 1, i, "+")
}
> x <- hilbert(1000)
> system.time(svd(x)) # svd toma vantagem de multi-threading
   user  system elapsed 
  3.907   0.012   3.969 # meu pc no Manjaro não é tão bom pois não tem o MKL do intel hahahaha
```
Quando tiver que usar **system.time** em expressões maiores temos:
```
system.time({
    n <- 1000
    r <- numeric(n)
    for(i in 1:n){
       x <- rnorm(n)
       r[i] <- mean(x)
    }
})
   user  system elapsed 
  0.096   0.000   0.097 
```
O problema de `system.time()` para otimização é que pressupõe-se que saiba aonde procurar. O que pode até ser verdade para programa pequenos, onde poderá vir a ter uma boa noção de onde o programa precisa de ser otimizado. Como fazemos para sabermos onde iniciar a nossa procura no código por locais menos otimizados nos casos menos simples?

>TESTE: Meu Linux Manjaro antes de instalar MKL
```
> set.seed(1)
> m <- 10000
> n <- 2000
> A <- matrix(runif (m*n),m,n)
> system.time(S <- svd (A,nu=0,nv=0))
   user  system elapsed 
 62.964   0.073  63.761 
```















