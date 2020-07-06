# f1 = f2 = 1
n =35

# print(f1, end=' ')
# print(f2, end=' ')

# for i in range(2, n):
# 	f1, f2 = f2, f1 + f2
# 	print(f2, end=' ')


def fib_speed(n):
	f1 = f2 = 1
	for i in range(2, n):
		f1, f2 = f2, f1 + f2
	return f2

print(fib_speed(34))
print('\n')


def fib_rec(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib_rec(n-1) + fib_rec(n-2)

# for i in range(0, n):
# 	print(fib_rec(i), end=' ')

print(fib_rec(33))


import math

golden_ration = (1 + math.sqrt(5)) / 2

def fib(n):
	result = (golden_ration**n - (1 - golden_ration)**n) / math.sqrt(5)
	return round(result)

print('\n')
print(fib(34), '\n') #только до n = 70


def fib_python_way():
	f1, f2 = 0, 1

	while True:
		yield f1
		f1, f2 = f2, f1 + f2

for i, f in zip(range(n+1), fib_python_way()):
	print("{i:3}: {f:3}".format(i=i,f=f))
