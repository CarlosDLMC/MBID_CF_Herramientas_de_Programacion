array = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def snail(array):
    res = []
    while array:
        res += array.pop(0)
        array = list(zip(*array))[::-1]
    return res

def condition(a, b, n):
    s = 0
    for i in range(n + 1):
        if i in (a, b):
            continue
        s += i
    print(s, (n * (n + 1) / 2))

def remov_nb(n):
    l = 0
    r = n
    sum_total = (n * (n + 1) / 2)
    # sum_total = sum([i for i in range(n + 1)])
    res = list()
    while l < r:
        s = sum_total - l - r
        m = l * r
        if m > s:
            r -= 1
        elif s > m:
            l += 1
        else:
            res.append((l, r))
            res.append((r, l))
            r -= 1
    return res

def reverse_array(ar):
    l = 0
    r = len(ar) - 1
    while r > l:
        ar[r], ar[l] = ar[l], ar[r]
        r -= 1
        l += 1
    return ar

print(reverse_array([1, 2, 3, 4]))
