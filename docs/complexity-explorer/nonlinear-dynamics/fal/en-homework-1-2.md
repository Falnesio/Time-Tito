# Homework 1.2 Maps and difference equations

## Question 1

Calculate the third iterate of the logistic map with _r_ = 2.5 starting from _x0_ = 0.5.  Do this by hand.  What is the third iterate you calculated?  \(Choose the one that's closest; different computers and calculators do arithmetic slightly different, so your answer may vary a bit\).  
for $$x_{0}=0.2$$ and R = 2:

> | $$x_{1}$$ | $$R*x_{0}(1-x_{0})$$ |
> | :--- | :--- |
> |  | 2.5\(0.5\)\(1 - 0.5\) |
> |  | 0.625 |
> | $$x_{2}$$ | 2.5\(0.625\)\(1 - 0.625\) |
> |  | 0.5859375 |
> | $$x_{3}$$ | 2.5\(0.5859375\)\(1-0.589375\) |
> |  | 0.601501464844 |
> | $$x_{4}$$ | 2.5\(0.601501464844\)\(1-0.601501464844\) |
> |  | 0.59924363158 |
> | $$x_{5}$$ | 2.5\(0.59924363158\)\(1-0.59924363158\) |
> |  | 0.60037675397**       &lt;- Fixed Point** |

```
r = float(input("Insert r value: "))
x = float(input("Insert starting x value: "))
n = float(input("Insert number of iterations: "))
i = 0

while i < n:
	x = r*x*(1-x)
	i += 1

print(x)

```



