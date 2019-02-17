# Anotações Fal

## R Programming

### Semana 2

#### Control Structures - Introduction
Ao invés de *loop* estarei usando o termo **ciclo**.

Estruturas de controle em R permite controlar a corrente de execução do programa, dependendo das condições da fase de execução (**runtime**). Tais estruturas são...
 1. **if, else**: para testar uma condiçaão
 2. **for**: para executar um ciclo uma quantidade fixa de vezes
 3. **while**: para executar um ciclo caso condição seja verdadeira
 4. **repeat**: para executar um ciclo infinito
 5. **break**: para quebrar ou parar um ciclo
 6. **next**: para pular a próxima iteração do ciclo
 7. **return**: para sair de uma função

Tipicamente não utilizamos tais comandos no terminal e sim ao escrever um **script** (um programa estruturado pronto para utilização).

##### Controle Structures: if-else
```
if(condição){
        executar isso caso a condição seja verdadeira
} else if {outra condição} {
        executar isso caso apenas a segunda condição seja verdadeira
} else {
        executar isso caso contrário
}
```
**if**
```
# A condição pode vir por fora 
if(x > 3){
        y <- 10
} else {
        y <- 0
}

# ou por dentro
y <- if(x > 3){
        10
} else {
        0
}

# isso facilita enxergar qual o propósito do bloco condicional
```
**else**
*Else* não é obrigatório, caso uma condição *if* não funciona, nada acontece.

##### Control Structures - For loops
Um dos mais comuns a serem utilizados, tipicamente temos um índice i (pode ser qualquer vetor de caracteres mas tipicamente usa-se a letra i) que passa por uma sequência, executando o código dentro do ciclo para cada iteração. A sequência pode ser de elementos de qualquer classe.
```
for(i in 1:10){
        print(i)
}
```
Ou seja, primeiro i = 1, executa print(1), depois i = 2, executa print(2)...

**seq_along(a)** criar uma sequência de inteiros com o mesmo tamanho que a. Pode ser usado como guia para o índice no ciclo for
`for(i in seq_along(a)`.

Ciclos for com apenas um comando não precisão de `{}`. Podemos escrever, por exemplo, `for(i in 1:4) print(i)`.

Também é possível colocar ciclos for dentro de ciclos for.

**seq_len(nrow(x))** ou **seq_len(ncol(x))** permitem contar o número de linhas ou colunas de uma matriz. 

##### Control Structures - While loops

While pega uma expressão lógica e executa dependendo da veracidade de tal expressão. Ela permite a criação de ciclos que continuam infinitamente até haver uma contradição da condição. Caso não haja, ela nunca para.
```
n <- 3
p <- TRUE
while(n > 0 && p == TRUE){
        n <- n - 1
}
```
**rbinom()** é um gerador de números aleatórios.

##### Control Structures - Repeat, Next, Break

A única forma de parar um ciclo de **repeat** é colocando um **break**. Caso contrário era continua infinitamente.
```
x <- 0
repeat{
        x <- x + 1
        if(x > 10){
                break
        }
}
```
Imagine que queremos pular as primeiras 20 iterações de um ciclo for.
```
for(i in 1:100){
        if(i <= 20){
                next
        }
        código que faz alguma coisa, blah blhablha
}
```
**Return** geralmente é utilizado para sair de uma função e retornar um valor passado a ela. Ela pode ser usada para sair de um ciclo também.

Para quando estiver utilizando o terminal e quero aplicar algo ciclo, existem alguns comandos *apply que funcionam melhor do que as estruturas de controle demonstradas aqui.

#### Your First R Function
Para criar uma função é muito simples
```
# no caso do input2 abaixo, se não for preenchido o valor default é 4
# os inputs são referencias internas usadas pela função, existem apenas dentro da função.
nome_da_função <- function(input1, input2 = 4, input3, ...){
                o que a função faz
}
adicionar2 <- function(x, y){
              x + y
}
acimade10 <- function(x){
              usar <- x > 10
              x[usar]
}
acimede <- function(x,n){
            usar <- x > n
            x[usar]
}
mediacols <- function(x, removeNA = TRUE){
              colunas <- ncol(x)
              medias <- numeric(colunas)
              for(i in 1:colunas){
                      medias[i] <- mean(x[,i], na.rm = removeNA)
                      # na.rm é argumento de mean
              }
              medias
}
```

#### Functions (part 1)

Funções são objetos R com classe function, portanto podem ser tratados como qualquer outro objeto R. Funções possuem **argumentos nomeados** com valores default potenciais (caso seja aplicado argumento = valor).

**Argumentos formais** são aquelas definidas explicitamente dentro do corpo da função, referenciadas no início.

**formals()** mostra todos os argumentos formais dentro de uma função.

A ordem ou nome dos argumentos numa função é importante. Na função acimde(), o primeiro argumento é uma sequência que preenche *x* e o segundo um valor escalar que preenche *n*. Caso queira troca a ordem de inserção dos argumentos, terá que nomeá-los, por exemplo acimade(n=2, x=1:5). Todavia, se um argumento for nomeado e outro não, apenas sobra mais um então o segundo não necessariamente teria que ser nomeado.

Não é recomendado mas se escrever apenas parcialmente o nome de um argumento e esse tiver apenas um correspondente, o sistema R reconhece a referência.

O sistema ao procurar pelos argumentos na função, primeiro procura por um nome identico, depois pelo nome parcial e depois pela posição.

#### Functions (part 2)

Quando num argumento é aplicado NULL como default, significa que não há nada (conjunto vazio).

##### Lazy Evaluation

Lazy evaluation ou **avaliação preguiçosa** significa que os argumentos são apenas analisados enquanto são utilizados.
Portanto a função:
```
f <- function(a, b){
        a^2
}
```
Ao `f(2)` ser utilizada, não utiliza b, não mostra erro.
```
imprimir2 <- function(a, b){
        print(a)
        print(b)
} 
```
Ao ser utilizada, `imprimir2(45)` executa porém mostra erro depois de imprimir 45.
`Error in print(b) : argument "b" is missing, with no default`

##### ...
O argumento **...** é usado para absorver inúmeros outros argumentos de outra função com seus devidos valores default.
```
myplot <- function(x, y, type = "l", ...){
        plot(x, y, type = type, ...)
}
```
Em **funções genéricas**, o **...** é usado para passar argumentos extras para métodos de diferentes tipos de dados (mais a frente tem explicação melhor).

É utilizado também quando não é sabido a quantidade de argumentos que uma função vai tomar, então aparece como o primeiro argumento (vide args(paste) e args(cat)). Quando isso acontece, todo argumento que vem depois tem que ser nomeado, nã será reconhecido seu posicionamento e nem seu nome parcial.

#### Scoping Rules - Symbol Binding

Como R sabe qual símbolo corresponde a determinado valor?
```
lm <- function(x){ x * x }
```
`lm` já existe, então com R sabe qual chamar, a minha função ou a preexistente?

**environments** são coleções de pares de símbolos e valores.

Quando aplicamos um símbolo, R busca nos seus **environments** (ambientes) por algo correspondente, primeiro o Global, depois os pacotes instalados até o pacote base. Isso acontece até atingir o **empty environment** e apresentar o erro de objeto não encontrado.

`.GlobalEnv` é o seu ambiente de trabalho atual, incluindo as variáveis que nomeou, por exemplo o `lm` que definiu.

Quando uma bibliotexa é carregada, ela se posiciona como segunda na lista e todo o resto desce um nível.

**search()** mostra lista de environments em ordem. O pacote base sempre é o último pacote.

Quando se tem uma **variável livre** dentro de uma função, ou uma variável sem referência interna, R busca correspondência através da lista.

**Lexical Scoping** ou **Static Scoping** significa que R busca correspondência de *variáveis livres* dentro do *ambiente* em que a função foi gerada.

Uma **function closure** é criada quando uma função é associada a um **environment ** em R.

##### Scoping Rules - R Scoping Rules

Usualmente variáveis livres estão presentes e definidas no ambiente global. Todavia podemos definir funções dentro de outra função ou ter uma função como um valor de retorno, definido dentro da função anterior.

Geralmente isso acontece dentro do contexto de **constructure functions**, ou funções que constroem outras funções.
```
make.power <- function(n){
        pow <- function(x){
                x^n
        }
}
```
Sendo n uma variável livre dentro de pow, R busca primeiro no seu **parent environment**, ou ambiente genitor: make.power.

A função gerada make.power constroi funções que podem depois serem usadas para obter diferentes potenciações:
```
> quadrado <- make.power(2)
> quadrado(3)
[1] 9
```
Testando, a resposta é 120. Por ser lexical e não dinâmico, R sempre busca dentro da hierarquia demonstrada para cada função dentro de onde foi gerado. Caso fosse **dinâmico**, g(x) puxaria informação sobre y de acordo com o local onde foi chamado (função f) e não no ambiente onde foi definido (global).
```
y <- 10
f <- function(x){
        y <- 2
        y * 2 * g(x)
}
g <- function(x){
        x * y
}
f(3)
```
Em lexical scoping, todos os objetos estão guardados na memória. Todas as funções carregam um link ao seu ambiente genitor. Isso tudo é comum à maioria das linguagens de programação atuais.

##### Scoping Rules - Optimization 

Algumas funções de otimização em R como `optim`, `nlm` e `optimize` necessitam que você passe uma função no qual o argumento é um vetor de parâmetros. `optimize` otimiza apenas para um valor.

Por exemplo, terá uma função que gostaria de minimizar ou maximizar dentro de um grupo de parâmetros as funções mencionadas anteriormente pegam essas funções e procuram um máximo ou mínimo. Quando trabalhando com estatística, tais otimizações dependem não só das funções e parâmetros mas dos dados. Como escrevemos um programa de forma limpa e clara de tal modo que facilite a vida do usuário?

Em muitos casos é desejável manter alguns desses parâmetros fixos e otimizar pelos outros.

Na resolução de um problema de otimização em R, a ideia básica é crir uma *função construtura*, que constroi a função objetiva. Nessa função objetiva todos os dados e determinantes estão definidos etc. para não ser necessário especificar tais objetos toda vez que for chamar a função. A punica coisa que necessitaria de especificar seria os valores dos parâmetros.

> funções de otimização em R minimiza funções, então terá que usar o negativo das funções para maximizações.

O exemplo abaixo precisa de conhecimento sobre funções de máxima verossimilhança. Uma revisão sobre o assunto pode ser obtida atraveś [desse vídeo de 20 minutos em inglês](https://www.youtube.com/watch?v=Dn6b9fCIUpM). O vídeo é claro e lento, então mesmo nao sabendo inglês tem como obter uma boa ideia do que ocorre.

A função abaixo gera uma função negativa log-likelyhood.
```
make.NegLogLik <- function(data, fixed=c(FALSE,FALSE)) {
        params <- fixed
        function(p) {
                params[!fixed] <- p
                mu <- params[1]
                sigma <- params[2]
                a <- -0.5*length(data)*log(2*pi*sigma^2)
                b <- -0.5*sum((data-mu)^2) / (sigma^2)
                -(a + b)
        } 
}
```
Testando usando 100 observações gerados aleatoreamente com **média 1** e **desvio padrão 2**. A semente que gera os mesmos valores aleatórios é 1.
`> set.seed(1); normals <- rnorm(100, 1, 2)`
E criamos a função com os dados 
```
> nLL <- make.NegLogLik(normals)
> nLL
function(p) {
                params[!fixed] <- p
                mu <- params[1]
                sigma <- params[2]
                a <- -0.5*length(data)*log(2*pi*sigma^2)
                b <- -0.5*sum((data-mu)^2) / (sigma^2)
                -(a + b)
        }
<bytecode: 0x8d2c570>
<environment: 0x664b210>
```
A função foi criada com um link para o local na memoria onde está guardada em forma de código hexadecimal. Através disso que R consegue localizar tal objeto e em qual ambiente está localizado.

Olhando os componentes do ambiente referente à função (o **enclosing environment**) encontramos
```
> ls(environment(nLL))
[1] "data"   "fixed"  "params"
```
Todos esses objetos são variáveis livres dentro da função, mas são definidos no mesmo ambiente da função.

Rodando a otimização com valores iniciais mu =0 e sigma = 1
```
> optim(c(mu = 0, sigma = 1), nLL)
$par
      mu    sigma 
1.218239 1.787343 

$value
[1] 199.9697

$counts
function gradient 
      65       NA 

$convergence
[1] 0

$message
NULL
```
Esse resultado é bem próximo ao real com **média 1** e **sigma 2**.

Podemos também criar uma função com um desses parâmetros fixos para tentar resolver para o parâmetro livre. Vamos testar com **sigma fixo em 2**.
```
> nLLsigma <- make.NegLogLik(normals, c(FALSE, 2))
> nLLsigma
function(p) {
                params[!fixed] <- p
                mu <- params[1]
                sigma <- params[2]
                a <- -0.5*length(data)*log(2*pi*sigma^2)
                b <- -0.5*sum((data-mu)^2) / (sigma^2)
                -(a + b)
        }
<bytecode: 0x8d2c570>
<environment: 0xc098ac8>
```
Vamos otimizar testando o parâmetro livre de -1 a 3.
```
> optimize(nLLsigma, c(-1,3))
$minimum
[1] 1.217775

$objective
[1] 201.1433
```
Agora testando com **mu fixo em 1** e sigma variando de 1e-6 a 10.
```
> nLLmu <- make.NegLogLik(normals, c(1,FALSE))
> nLLmu 
function(p) {
                params[!fixed] <- p
                mu <- params[1]
                sigma <- params[2]
                a <- -0.5*length(data)*log(2*pi*sigma^2)
                b <- -0.5*sum((data-mu)^2) / (sigma^2)
                -(a + b)
        }
<bytecode: 0x8d2c570>
<environment: 0xd98e448>
> optimize(nLLmu, c(1e-6, 10))
$minimum
[1] 1.800596

$objective
[1] 200.7065
```

###### Plotando

Para ver o resultado de diferentes valores possíveis para a função nLLsigma e nLLmu, aplicamos uma determinada sequência à variável x, que representará os valores a serem testados de sigma e mu.

Depois  utilizamos `sapply(a, b)` que aplica a função **b** aos valores **a** e guardamos em y.

Após isso só resta aplicar a seguinte função para projetar o gráfico: `plot(x, exp(-(y - min(y))), type = "l")`.

Testando valores de **Sigma**
```
x <- seq(1.7, 1.9, len = 100)
y <- sapply(x, nLLmu)
plot(x, exp(-(y - min(y))), type = "l")
```
Testando valores de **Mu**
```
x <- seq(0.5, 1.5, len = 100)
y <- sapply(x, nLLsigma)
plot(x, exp(-(y - min(y))), type = "l")
```
Brincando tem até como criar uma função para automatizar isso
```
plotLL <- function(x1, x2, func = nLL){
        x <- seq(x1, x2, len = 100)
        y <- sapply(x, func)
        plot(x, exp(-(y - min(y))), type = "l")
}
```
Com lexical scoping, fica muito fácil encapsular funções e reutilizar objetos importantes.

#### Coding Standards

Padrões ajudam manter uma estrutura legível entre códigos de diferentes programadores. Cada programador tem seu estilo, mas isso não significa que não exista uma ordem no meio da doideira de todos que permita um certo grau de comunicação.

1. Primeiro Princípio de qualquer lingupagem de programação.
O código deve ser escrito utilizando um editor de texto e deve ser salvo como um arquivo de texto de tal forma que qualquer programa de edição possa editar e ler.

2. Indentar o código
Isso facilita a visualização do código e permite entender a hierarquia dos blocos de código: qual está dentro de qual.

3. Limita o tamanho das linhas de código
Códigos com linhas muito grandes geram confusão e necessitam que quem esteja lendo deixe de ver parte do código para ver o resto.

Esses últimos dois princípios influencia o programador a escrever códigos mais eficiente e sucintos.

4. Limita o tamanho das funções
Uma função deveria fazer apenas uma coisa e tal coisa tem que ser claro. Quando se tem várias funções com objetivos claros, quando algo errado acontece saberá exatamente onde e o porquê.

#### Dates and Times

Existe uma classe para datas (`Date`) e tempo (`POSIXct` e `POSIXlt`) em R. Datas estão no formato ano-mes-dia e são guardadas internamente como um número, sendo 0 1970-01-01, incrementando 1 para cada dia após tal data. Tempo é guardado como um número, sendo 0 a data anterior, incrementando 1 para cada segundo após tal data. Datas e tempos anteriores são números negativos.

**POSIXct** guarda o tempo comoum número inteiro.

**POSIXlt** guarda o tempo como uma lista de valores.

**Sys.time()** mostra o tempo presente

Tendo datas no formato apropriado, torna mais fácil adicionar datas, compara datas (vr qual pe maior) etc. As datas levam em conta irregularidades como anos bissextos e diferentes longitudes. As funções de gráfico geralmente reconhecem a classe de data e tempo.

Aplicando o presente a x, e depois POSIXlt a x, podemos explorar a estrutura de POSIXlt.
```
> x <- Sys.time()
> x
[1] "2019-02-14 19:04:02 -02"
> p <- as.POSIXlt(x)
> p
[1] "2019-02-14 19:04:02 -02"
> unclass(p)
$sec
[1] 2.883164

$min
[1] 4

$hour
[1] 19

$mday
[1] 14

$mon
[1] 1

$year
[1] 119

$wday
[1] 4

$yday
[1] 44

$isdst
[1] 1

$zone
[1] "-02"

$gmtoff
[1] -7200

attr(,"tzone")
[1] ""    "-03" "-02"
```

**strptime()** converte um vector de caracteres em POSIXlt. É necessário mostrar a formação, declarando o que cada objeto dentro do vetor de caracteres representa. No caso %B, %d, %Y, %H e %M representam respectivamente mes, dia, ano, hora e minuto.
```
data <- c("January 10, 2012 10:40", "December 9, 2011 9:10")
x <- strptime(data, "%B %d, %Y %H:%M")
```

É possível transformar um vetor de caracteres em data da seguinte forma:
```
x <- as.Date("1970-01-01")
```
Caso imprima x, os caracteres apareccerão, poreḿ esse não é o valor real guardado.

Digitando `unclass(x)` obteremos o valor real.

Existem algumas funções genéricas que funcionam para delimitar períodos também.

**weekdays()** dar um dia da semana

**months()** dar o nome de um mes

**quarters()** dar o nome de semestres ("Q1", "Q2", "Q3", "Q4")

