# Practical R Exercises in swirl 2

## Introduction to [Swirl](http://www.swirlstats.com)

### Logic

Statements can either be TRUE or FALSE. We may use parenthesis to determine the order of comparisons, such as `(TRUE == FALSE) == FALSE` which is TRUE. Other logical operators include >, <, <=, >=, and != (different than). Exclamation is a not operator, that means in conjuntion with a logical object, the object will become it's opposite.

Things on the left of an operator are left operand, similarly things on the right are right operands.

AND operator are `&` and `&&`. The first can evaluate vectors, the second only evaluates the first member of a vector. 
Therefore `TRUE & c(TRUE, FALSE, FALSE)` is actually `TRUE & TRUE`, `TRUE & FALSE`, `TRUE & FALSE` and equivalent to 
`c(TRUE, TRUE, TRUE) & c(TRUE, FALSE, FALSE)`.

OR operators `|` and `||` follow the same rule.

Order of logical operations dictates that **ALL** AND operators are resolved before OR.

**isTRUE()** checks if statement is TRUE.

**xor()** only if one argument evaluates to TRUE and the other to FALSE, will this function will return TRUE.

**any()** returns TRUE if any element in the vector is TRUE

**all()** returns TRUE if every element is TRUE

**identical()** compares two objects.

**sample(x)** creates a random sampling of x integers from 0 to x.

**which()** takes a logical vector and returns the indices of the TRUE statements.

### Functions

**sd()** brings up the standard deviation.

**Anonymous functions** are functions that are not named.

Functions may be called before being properly defined. Example being:
```
evaluate <- function(func, dat){
  func(dat) 
}

evaluate(function(x){x+1}, 6)
```

Creating arguments on the fly to add to function:
```
mad_libs <- function(...){
  # Do your argument unpacking here!
  args <- list(...)
  place <- args[["place"]]
  adjective <- args[["adjective"]]
  noun <- args[["noun"]]
  # Don't modify any code below this comment.
  # Notice the variables you'll need to create in order for the code below to
  # be functional!
  paste("News from", place, "today where", adjective, "students took to the streets in protest of the new", noun, "being installed on campus.")
}
```

From one of the exercises, **how to make a binary operator:**
```
# User-defined binary operators have the following syntax:
#      %[whatever]% 
# where [whatever] represents any valid variable name.
# 
# Let's say I wanted to define a binary operator that multiplied two numbers and
# then added one to the product. An implementation of that operator is below:
#
# "%mult_add_one%" <- function(left, right){ # Notice the quotation marks!
#   left * right + 1
# }
```

### Dates and Functions

