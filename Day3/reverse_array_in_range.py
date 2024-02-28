
def reverser_array(A, i, j):
    while i < j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

        i += 1
        j -= 1
    return A

A = [1, 2, 3,  4]
i = 2
j = 3
reverser_array(A , i, j)
print(A)