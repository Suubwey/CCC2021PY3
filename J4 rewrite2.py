books = input()

L = books.count("L")
M = books.count("M")
S = books.count("S")

booksLength = L+M+S
correctBooks = "L" * L + "M" * M + "S" * S
errors = 0
swaps = 0

for i in range(booksLength):
	if correctBooks[i] != books[i]:
		errors += 1

if errors % 2 == 1:
	swaps += 2
	errors -= 3

swaps += errors // 2

print(swaps)