def reverse_string(str):
    return str[::-1]

def reverse_string2(str):
    res = ""
    for i in range(len(str)):
        res += str[len(str) - 1 - i]
    return res

print(reverse_string2("Hola"))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

def sum_matrix(matrix):
    res = 0
    for line in matrix:
        for element in line:
            res += element
    return res

def sum_matrix2(matrix):
    res = 0
    for line in matrix:
        res += sum(line)
    return res
print(sum_matrix(matrix))
print(sum_matrix2(matrix))

def two_sum(array, num):
    array.sort()
    solutions = list()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] > num:
            right -= 1
        elif array[left] + array[right] < num:
            left += 1
        else:
            solutions.append(f"{array[left]} + {array[right]} = {num}")
            left += 1
    return solutions

def two_sum2(array, num):
    numbers = dict()
    solutions = list()
    for n in array:
        numbers[num - n] = n
        if n in numbers:
            solutions.append(f"{n} + {numbers[n]} = {num}")
    return solutions

ar = [1, 3, 5, 6, 11, 23]

print(two_sum(ar, 9))
print(two_sum2(ar, 9))
