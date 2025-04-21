import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    m = len(a)
    if m == 0:
        return []

    n = len(a[0])

    if m*n != new_shape[0]*new_shape[1]:
        return []

    i = 0
    j = 0

    reshaped_matrix = []
    for k in range(new_shape[0]):
        new_row = []
        for l in range(new_shape[1]):
            new_row.append(a[i][j])
            if j == n - 1:
                j = 0
                i = i + 1
            else:
                j = j + 1
        reshaped_matrix.append(new_row)

    return reshaped_matrix


print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))
print(reshape_matrix([[1,2,3],[4,5,6]], (3, 2)))