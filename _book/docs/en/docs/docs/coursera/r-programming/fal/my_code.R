# No console digite source('my_code.R')
# para chamar as seguintes funções
# Digite ls() para ver funcções existentes

my_function <- function(){
  x <- rnorm(100)
  mean(x)
}

second_function <- function(x){
  x + rnorm(length(x))
}