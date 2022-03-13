matrix = [
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0]
]

def print_matrix(m):
    print("matrix:")
    for line in m:
        print(line)

def mark_visited(m, x, y, total):
    if m[y][x] == 1:
        m[y][x] = 2
        total[0] += 1
    else:
        return
    if y < len(m) - 1:
        mark_visited(m, x, y + 1, total)
    if y > 0:
        mark_visited(m, x, y - 1, total)
    if x < len(m[0]) - 1:
        mark_visited(m, x + 1, y, total)
    if x > 0:
        mark_visited(m, x - 1, y, total)

def get_rivers(m):
    sizes = list()
    total = [0]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                mark_visited(m, j, i, total)
                sizes.append(total[0])
                total[0] = 0
    return sizes


print(get_rivers(matrix))
