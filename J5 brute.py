row = int(input())
col = int(input())
k = int(input())

board = [[False] * col for i in range(row)]

# def printboard():
# 	global board
# 	for i in board:
# 		print(i)

# printboard()
for i in range(k):
	d, n = input().split()
	n = int(n)-1
	if d == "R":
		for j in range(col):
			board[n][j] = not board[n][j]
		# printboard()
	else:
		for j in range(row):
			board[j][n] = not board[j][n]
		# printboard()

count = 0

for i in board:
	count += i.count(True)

print(count)