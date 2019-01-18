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
vetores contêm apenas objetos da mesma classe (exceto listas)
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
```

