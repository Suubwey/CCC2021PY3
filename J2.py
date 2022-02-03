N = int(input())

hp = ""
hb = 0

for i in range(N):
    p = input()
    b = int(input())
    if b > hb:
        hp = p
        hb = b

print(hp)