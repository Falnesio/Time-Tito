# Practical R Exercises in swirl

## Introduction to [Swirl](http://www.swirlstats.com)

### Basic Building Blocks 

**S.W.I.R.L or Statistics With Interactive R Learning** was developed by a 
student at the John Hopkins department of biomechanics, Nick Carchedi.

**Data Structure: ** any object that contains data. Numeric vectors are the simplest type of data structure in R. A number is considered a vector of length one.

**c(), concatenate or combine**, creates a vector.
You can assign any number of operations to a vector and they will be applied iteratively to each element.
If z <- c (1, 2, 3), z * 2 + 100 is this: z * c(2, 2, 2) + c(100, 100, 100). 
c(1, 2, 3, 4) + c(0, 10) is really c(1, 2, 3, 4) + c(0, 10, 0, 10)
[1]  1 12  3 14
This is called **vector recycling**.
When one vector does not divide by the other, R warns us.

**?**function-name brings out the guide on said function.
If a função is a symbol you have to use backqoutes. --ex. ?`:`--

### Workspace anf Files

**getwd()** finds working directory
**setwd** sets working directory
**ls()** lists current variables
**list.files() or dir()** lists all files in current directory
**file.create()** creates a file
**file.exists()** checks existence of file
**file.info()** checks info on file
You can use the $ operator --- e.g., file.info("mytest.R")$mode --- to grab specific items.
**file.rename** renames files
**file.remove** deletes files
**file.copy** copies files
**file.path** shows relative file path
You can use file.path to construct file and directory paths that are independent of the operating system your R code is running on.

Create a directory in the current working directory called "testdir2" and a subdirectory for it called "testdir3", all in one command by using dir.create() and file.path().

*dir.create(file.path("testdir2","testdir3"), recursive=TRUE )*

### Sequences and Numbers

**number1:number2** is used to create a sequence of numbers from number1 to number2.
Numbers are added on, one by one from number1 to number2 even is number1 is irrational.
If number1 < number2 then the numbers go down increments of one.

**seq(first, last, by=increment (or) length=size)** does the same thing.

**rep(a, b)** repeats a, b times.
"a" can be a vector sequence that is repeated *rep(a, times=b)*, or where each item in the vector is repeated b times *rep(a, each=b)*.

### Vectors

**Atomic Vectors**
 * Single Data type
  * numeric
  * logical
   * TRUE (1), FALSE (0), NA (Not available)
   * They appear through logical conditions which use logical operators.
   * *logical operators:* >, <, <=, >=, ==, !=
   * A | B = A ou B; A&B = A e B; !A =  não A 
  * character
  * integer
  * complex
 
**Lists**
 * Multiplie data types

**paste()** collapses a sequence of characters in a vector.
**paste()** prints and joins character vectors.

*Always remeber the affects of vector recycling* 
```
> paste(1:3, c("X", "Y", "Z"), sep="")
[1] "1X" "2Y" "3Z"
```
### Missing Values

**NA** are missing values. They will not suffer the effects of math operations.

**NaN** means *not a number*. IT is the result of operations such as deviding zero by zero (0/0) or subtracting infinity from infinity (Inf - Inf).

**rnorm(h)** draws h random numbers from a normal distribution  
**sample(b, a)** draws a random sample size a from data b 
**is.na(f)** returns TRUE if NA condition in relation to the collection f

Since TRUE are ones and FALSE are zeros, the sum shows TRUE's frequency.

### Subsetting Vectors

Index vectors come in four flavours:

1. Logical Vectors
2. Vectors of Positive Integers
3. Vectors of Negative Integers
4. Vectors of Character Strings

**x[1:10]** brings about the first 10 elements in x for it brings up the numbers by the indices 1 through 10.
R uses one-based indexing so indices start with 1.
If you ask R something that is not in the boundaries of x, there will be no error. It will bring forth either NA or a numeric 0.

**x[c(-2, -10)]** brings us everything except element with index 2 and 10. Same with **x[-c(2, 10)]** and **x[-2 & -10]** etc.

**x[is.na(x)]** brings about a subset of all NAs in x

**x[!is.na(x)]** brings all the elements that are not NA in x

Logical operations bring out logical vectors. Placing logical vectors in keys after a avariable makes a selection in the variable to create a subset based on the logical operation inside the keys.


**Named Elements**

**c(nome = element)** create an element with name "nome".

**names(x)** finds names in vector.

**names(x) <-** places names in vectors.

**identical()** chehcks if two variables are the same

We can call on vectors by name --ex. x[c("bar", "foo")]--


### Matrices and Data Frames

Matrices and Data frames represent rectangular data types: they store tabular data.
Matrices contain only one class of data while Data Frames do not have that limit.

**dim()** brings up the dimension of th vector. We can also use it to apply a dimension.
**attributes()** brings up vector attributes.

**class()** brings up class of variable

**matrix()** creates a matrix.

**cbind()** binds coloumn to matrix/data table

Coersion is when all elements in a vector transform into the same class. This happens when you try to place differently classed elements in a matrix, for example.

**length()** shows the length of the vector.

**data.frame()** creates a data frame.

**colnames(x) <-** creates coloumn names for the data table x.

