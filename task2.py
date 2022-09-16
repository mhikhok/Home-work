n = int(input())

for i in range(1, n+1):
    for _ in range(-1, n-i):
        print(i, end = ' ')
    print()
