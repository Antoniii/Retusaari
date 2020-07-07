# def fac(n):
# 	if n == 0:
# 		return 1

# 	return n * fac(n-1)

def double_fac(n):
	if n == 0 or n == 1:
		return 1

	return n * double_fac(n-2)


def easy_fac(n):
	if n == 0:
		return 1

	f = 1
	i = 0

	while i < n:
		i += 1
		f = f * i

	return f

def double_easy_fac(n):
	if n == 0 or n == 1:
		return 1

	if n % 2 == 0:
		k = n / 2
		temp = easy_fac(k) * 2**(k)
		f = temp
	else:
		k = (n-1) / 2
		temp = easy_fac(k) * 2**(k)
		f = easy_fac(n) / temp

	return f

n=11
print("{n}!! = {f}".format(n=n, f=double_fac(n)))
print("{n}!! = {f}".format(n=n, f=int(double_easy_fac(n))))