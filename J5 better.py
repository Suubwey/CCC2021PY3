row = int(input())
col = int(input())
k = int(input())

board = [[False] * col for i in range(row)]

rops = set()
cops = set()

for i in range(k):
	choice, n = input().split()
	n = int(n) - 1
	if choice == "R":
		if n in rops:
			rops.remove(n)
		else:
			rops.add(n)
	else:
		if n in cops:
			cops.remove(n)
		else:
			cops.add(n)

for i in rops:
	for j in range(col):
		board[i][j] = not board[i][j]
for i in cops:
	for j in range(row):
		board[j][i] = not board[j][i]

count = 0

for i in board:
	count += i.count(True)

print(count)