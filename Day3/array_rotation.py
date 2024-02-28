def reverser_array(A, i, j):
    while i < j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

        i += 1
        j -= 1
    return A

A = [1,2,3,4]
array = reverser_array(A, 0, len(A)-1)
print(array)
rotated_array = reverser_array(array, 2, len(A)-1)
print(rotated_array)