def draw(n):
    for i in range(n + 1):
        for j in range(i):
            print((i + j) % 2, end=" ")
        print()

draw(5)
