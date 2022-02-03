books = input()
# books = "LLSMLSLM"
L = books.count("L")
M = books.count("M")
S = books.count("S")

booksLength = L+M+S
# target = "L"*L+"M"*M+"S"*S
swaps = 0

# print(books)
# print(target+"\n")

for i in range(L):
	if books[i] == "S":
		for j in range(booksLength-S, booksLength):
			if books[j] == "L":
				books = books[:i] + "L" + books[i+1:]
				books = books[:j] + "S" + books[j+1:]
				swaps += 1
				print(books)
				break
		else:
			for j in range(i+1, booksLength):
				if books[j] == "L":
					books = books[:i] + "L" + books[i+1:]
					books = books[:j] + "S" + books[j+1:]
					swaps += 1
					break
	elif books[i] == "M":
		for j in range(booksLength-S-M, booksLength-S):
			if books[j] == "L":
				books = books[:i] + "L" + books[i+1:]
				books = books[:j] + "M" + books[j+1:]
				print(books)
				swaps += 1
				break
		else:
			for j in range(i+1, booksLength):
				if books[j] == "L":
					books = books[:i] + "L" + books[i+1:]
					books = books[:j] + "M" + books[j+1:]
					print(books)
					swaps += 1
					break


for i in range(L,L+M):
	if books[i] == "S":
		for j in range(booksLength-S, booksLength):
			if books[j] == "M":
				books = books[:i] + "M" + books[i+1:]
				books = books[:j] + "S" + books[j+1:]
				print(books)
				swaps += 1

print(swaps)

# books.index

# for i in range(L+M+S):
#     if books[i] == "L"