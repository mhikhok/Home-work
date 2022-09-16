n = int(input())

for i in range(n, 0, -1):
    y = i
    for _ in range(0, i):
        print(y, end = ' ')
    print()
