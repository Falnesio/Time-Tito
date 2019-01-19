# Anotações Fal

<a href="https://web.kamihq.com/web/viewer.html?state=%7B%22ids%22:%5B%221uR17bzdhrOsCAguSJDCYL1hTKBU3460R%22%5D,%22action%22:%22open%22,%22userId%22:%22110411010479911316355%22%7D">R Programming for Data Science - Peng Anotado</a>

<a href="https://web.kamihq.com/web/viewer.html?state=%7B%22ids%22:%5B%221EGA1ixBazpIdTNicjZTCnRLCPFkOu7J8%22%5D,%22action%22:%22open%22,%22userId%22:%22110411010479911316355%22%7D">Statistics and Computing - Chambers  Anotado</a>

## R Programming

```
x <- 5
x #prints 5
print(x) #prints 5

x <- 1:20
x #prints de 1 a 20
```

##### Existem 5 tipos de objetos básicos ou classes atômicas no R
1. caractere
1. numérico (ℝ)
1. inteiro
1. complexo 
1. lógico (T/F)

##### O mais básico de todos é o **vetor**
vetores contêm apenas objetos da mesma classe (exceto quando se trata de listas)
```
x <- vector() #cria um vetor vazio
x <- 1L #é um número inteiro 
1 / 0 #gera Inf que é infinito, na verade um número real grande
0 / 0 # gera NaN = Not a Number, não um número
```

##### Atributos
Objetos em R tem atributos
1. nomes, nomes de dimensões
1. dimensões
1. classe
1. tamanho (length)
1. metadados e demais atributos
```
attributes() #acessar atributos de um objeto
```

##### c(), concatenar, gerar vários objetos unidos
```
x <- c(0.5, 0.6) #vetor numérico
x <- 9:28 #vetor de inteiros
x <- c(2+0i, 4+3i) # vetor complexo

#coerção existe quando mais de uma classe está concatenada 
y <- c(1.7, "a") # tudo vira caractere
y <- c(TRUE, 2) # tudo vira numérico, no caso 1 e 2
y <- c("a", FALSE) # tudo vira caractere
```

##### coerção explícita, as.algo()
```
> x <- 0:6
> class(x)
[1] "integer"
> as.numeric(x)
[1] 0 1 2 3 4 5 6
> as.logical(x)
[1] FALSE TRUE TRUE TRUE TRUE TRUE TRUE
> as.character(x)
[1]  "0" "1" "2" "3" "4" "5" "6"

> x <- c("a", "b", "c")
> as.numeric(x)
[1] 
NA NA NA
Warning message:
NAs introduced by coercion
> as.logical(x)
[1] NA NA NA
> as.complex(x)
[1] NA NA NA
Warning message:
NAs introduced by coercion 
```

##### Criando uma lista 
```
x <-list(1, "a", 4 + 9i)
```
##### Matrizes
```
m <- matrix(nrow = 2, ncol = 3) # cria matriz vazia
m <- matrix(1:6, nrow = 2, ncol = 3) # cria matriz onde a11 = 1, a12 = 2, a21 = 3 etc.
dim(m) #imprime dimensões da matriz
attributes(m) # mostra atributos da matriz

# ao pegar uma lista, é possível torna-lá uma matriz:
lista <- 1:10
lista
numero_de_linhas <- 5
numero_de_colunas <- 2
dim(lista) <- c(numero_de_linhas, numero_de_colunas) # forçar uma dimensão na lista
lista

# é possível criar uma matriz de duas (ou mais) listas
x <- 1:3
y < 20:22
z <- 115:117
cbind(y,z,x) # cola as listas lado a lado como colunas na ordem definida
      y   z x
[1,] 20 115 1
[2,] 21 116 2
[3,] 22 117 3

rbind(y,z,x) # cola as listas de cima pra baixo em linhas
  [,1] [,2] [,3]
y   20   21   22
z  115  116  117
x    1    2    3
```
##### Factor, é um vetor de inteiros em que cada número tem um rótulo (ordenado ou não)
são importantes para funções como lm() e glm() para regressões
```
> f <- factor(c("yes", "yes", "no", "yes", "no"))
> f
[1] yes yes no  yes no 
Levels: no yes
> table(f)        # mostra a frequência de cada categoria
f
 no yes 
  2   3 
 > unclass(f)    # mostra os inteiros associados aos rótulos em ordem de acordo
 [1] 2 2 1 2 1   # com a lista concatenada original
attr(,"levels")
[1] "no"  "yes"  # mostra os rótulos em ordem do inteiro atribuído, 
                 # ou seja "no" = 1, "yes" = 2
```
É possível escolher quais rótulos são associados a cada inteiro
```
> f <- factor(c("yes", "yes", "no", "yes", "no"),
              levels = c("yes", "no"))
> f
[1] yes yes no  yes no 
Levels: yes no
> unclass(f)
[1] 1 1 2 1 2
attr(,"levels")
[1] "yes" "no" 
```
Sabendo que podemos forçar atributos a listas (ex. dim(lista) <- c(2,5))
podemos também atribuir qualquer ordenação de "levels" que quisermos após
a criação do vetor de fatores como o "f" criado anteriormente.
```
> f
[1] yes yes no  yes no 
Levels: yes no           # ou seja "yes" = 1 e "no" = 2
> levels(f) <- c("no", "yes")
> f
[1] no  no  yes no  yes
Levels: no yes          # ou seja "no" = 1 e "yes" = 2
> levels(f) <- c("yes", "no")
> f
[1] yes yes no  yes no 
Levels: yes no          # ou seja "yes" = 1 e "no" = 2
```
Assim podemos alterar até quais rótulos utilizamos
```
> levels(f) <- c("não", "sim")
> f
[1] não não sim não sim
Levels: não sim
> levels(f) <- c("batata", "manjericão")
> f
[1] batata     batata     manjericão
[4] batata     manjericão              # como vimos acima o [4] só significa que
Levels: batata manjericão              # é a continuação da lista começando pelo
                                       # 4º item.
```

##### Valores Inexistentes
NaN significa que valor numérico não existe
NA significa que não existe determinada coisa em geral
```
x <- (c(1, 2, NA, 10, 3))
# para testar se algo existe ou não podemos usar as funções
is.na(x)
# e
is.nan(x)
```
NaN necessáriamente é Na, todavia Na não é necessáriamente um número não existente,
portanto Na não necessáriamente é NaN.
```
x <- (c(1, 2, NAN, 10, 3))
# para testar se algo existe ou não podemos usar as funções
is.na(x)
# e
is.nan(x)
```

##### Data Frame
É uma traiz que aceita diferentes tipos de valores, ou seja
é uma tabela.
Cada linha na tabela pode ter um nome `row.names()` (o default são números começando 
pelo número 1), o que é bom para rotular diferentes observações na tabela. 
Tabelas podem ser criadas chamando `read.table()`, ou `read.csv()` 
para abrir um arquivo. 

Tabelas podem ser tranformadas em matrizes com `data.matrix()`, poreḿ sofreram coerção
e serão transformados no mesmo tipo de objeto.

Criando um Data Frame:
```
> x <- data.frame(foo = 1:4, bar = c(T, T, F, F))
> x
  foo   bar
1   1  TRUE
2   2  TRUE
3   3 FALSE
4   4 FALSE
```
`nrow(x)` pergunta sobre x o número de linhas
`ncol(x)` pergunta sobre x o número de colunas

##### Nomes
Todos os objetos em R podem ter um nome, um rótulo utilizando `names()`.
```
> x <- 1:3
> names(x) # dar erro pois nada foi atribuído
NULL
> names(x) <- c("João", "Maria", "José")
> x
 João Maria  José 
    1     2     3 
```
Vale lembrar que o exemplo acima não atribui os valores 1, 2 e 3 a João, Maria e
José, e sim que passamos a chamar 1, 2 e 3 de João, Maria e José. 
```
> names(x)
[1] "João"  "Maria" "José"
```
listas e matrizes podem ter nomes
###### listas
```
> z <- list(a = 1, b = 2, c =3)
> z
$a
[1] 1

$b
[1] 2

$c
[1] 3

> names(z)
[1] "a" "b" "c"
```
###### matrizes
No exemplo primeiro criamos uma matriz, para ter algo a trabalhar
```
> m <- matrix(1:6, nrow = 2, ncol = 3)
```
Daí criamos os nomes. Fazemos uma lista com duas concatenações: a **primeira** com os
nomes das **linhas** e a **segunda** com os nomes das **colunas**.
```
> dimnames(m) <- list(c("Loja da Solange","Loja da Fátima"),c("Preço do Computador","Preço da TV", "Preço do Laptop"))
> m
                Preço do Computador Preço da TV Preço do Laptop
Loja da Solange                   1           3               5
Loja da Fátima                    2           4               6
```




