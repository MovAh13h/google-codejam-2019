from math import sqrt

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def primeFactors(n):
	factors = []

	while n % 2 == 0: 
		factors.append(2)
		n = n / 2

	for i in range(3, int(sqrt(n))+1, 2): 
		while n % i == 0: 
			factors.append(int(i)) 
			n = n / i 
			  
	if n > 2: 
		factors.append(int(n))

	return factors

for i in range(1, int(input())+1):
	N, L = [int(i) for i in input().strip().split()]
	cipher = [int(i) for i in input().strip().split()]

	elms = []
	pairs = []

	for j in cipher:
		a, b = primeFactors(j)

		pairs.append([a, b])

		if a not in elms:
			elms.append(a)

		if b not in elms:
			elms.append(b)

	elms = sorted(elms)
	
	for j, k in enumerate(pairs):
		a, b = k

		try:
			if (b != pairs[j+1][0]):
				pairs[j+1][0], pairs[j+1][1] = pairs[j+1][1], pairs[j+1][0]
		except Exception:
			pass

	res = ""
	res += chars[elms.index(pairs[0][0])]

	for j in range(1, len(pairs)):
		res += chars[elms.index(pairs[j][0])]

	res += chars[elms.index(pairs[len(pairs)-1][1])]

	print('Case #{0}: {1}'.format(i, res))