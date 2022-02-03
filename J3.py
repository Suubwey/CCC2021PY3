direction = ''
nums = []
current = input()

while current != "99999":
    nums.append(current)
    current = input()


for num in nums:
    ts = int(num[0]) + int(num[1])
    if ts == 0:
        print(direction, end=' ')
    elif ts % 2 == 1:
        direction = "left"
        print(direction, end=' ')
    else:
        direction = "right"
        print(direction, end=' ')
    print(num[2:])