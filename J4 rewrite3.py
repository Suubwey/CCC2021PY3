books = input()

L = books.count("L")
M = books.count("M")
S = books.count("S")

booksLength = L+M+S
correctBooks = "L" * L + "M" * M + "S" * S
# print(correctBooks)
lm = ("L", "M")
ls = ("L", "S")
ms = ("M", "S")
ml = ("M", "L")
sm = ("S", "M")
sl = ("S", "L")

errors = {
	lm : 0,
	ls : 0,
	ms : 0,
	ml : 0,
	sm : 0,
	sl : 0,
}

for i in range(booksLength):
	if correctBooks[i] != books[i]:
		errors[(books[i], correctBooks[i])] += 1 

swaps = 0
leftover = 0

swaps += min(errors[lm], errors[ml])
leftover += abs(errors[lm]-errors[ml])
swaps += min(errors[ls], errors[sl])
leftover += abs(errors[ls]-errors[sl])
swaps += min(errors[ms], errors[sm])
leftover += abs(errors[ms]-errors[sm])

swaps += leftover // 3 * 2
print(swaps)
