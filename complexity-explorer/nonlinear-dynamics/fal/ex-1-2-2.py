r = input("Insert r value: ")
x = input("Insert starting x value: ")
n = input("Insert number of iterations: ")
i = 0

while i < n:
	x = r*x*(1-x)
	i += 1

print(x)
