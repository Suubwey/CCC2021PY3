books = input()

L = books.count("L")
M = books.count("M")
S = books.count("S")

booksLength = L+M+S
swaps = 0

for i in range(L):
	if books[i] == "S":
		for j in range(booksLength-1, 0, -1):
			if books[j] == "L":
				books = books[:i] + "L" + books[i+1:]
				books = books[:j] + "S" + books[j+1:]
				swaps += 1
				print(books)
				break
	elif books[i] == "M":
		for j in range(booksLength-1-S, 0, -1):
			if books[j] == "L":
				books = books[:i] + "L" + books[i+1:]
				books = books[:j] + "M" + books[j+1:]
				swaps += 1
				print(books)
				break
	else:
		continue
		

for i in range(L,L+M):
	if books[i] == "S":
		for j in range(booksLength-1, 0, -1):
			if books[j] == "M":
				books = books[:i] + "M" + books[i+1:]
				books = books[:j] + "S" + books[j+1:]
				swaps += 1
				print(books)
				break


print(swaps)
