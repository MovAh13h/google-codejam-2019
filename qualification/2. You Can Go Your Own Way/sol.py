T = int(input())

for i in range(1, T+1):
	N = int(input())
	lyndia = str(input())

	path = ''

	for move in lyndia:
		if move is 'S':
			path = path + 'E'
		else:
			path = path + 'S'

	print('Case #{0}: {1}'.format(i, path))