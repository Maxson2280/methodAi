def sum_main_diagonal(m):
    diag_elem = [m[i][i] for i in range(len(m))]
    diagonal_sum = sum(diag_elem)
    return diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_main_diagonal(matrix)
print("Сумма элементов на главной диагонали:", result)
