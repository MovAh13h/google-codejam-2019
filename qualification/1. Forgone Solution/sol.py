T = int(input())

def fourRemoval(a, b):
	index = 0
	
	sa = str(a)

	lengthA = len(sa)

	while index < lengthA:
		if sa[index] is "4":
			subtract = "4"

			for i in range(lengthA-index-1):
				subtract += str(0)

			a = a - int(int(subtract)/2)
			b = b + int(int(subtract)/2)

		index += 1

	if a is 0:
		a = a + 1
		b = b - 1

	sb = str(b)

	if sb.find("4") is not -1:
		a, b = fourRemoval(b, a)

	return a, b

for i in range(1, T+1):
	N = int(input())
	A, B = 0, 0

	if N % 2 is 0:
		A = int(N / 2)
		B = A

	elif N % 2 is 1:
		A = int(N // 2)
		B = A + 1

	A, B = fourRemoval(A, B)

	print('Case #{0}: {1} {2}'.format(i, A, B))
