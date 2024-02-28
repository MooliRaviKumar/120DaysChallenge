A = [3, 1, 2]
"""
Brute Force
"""
count = 0
for i in range(len(A)):
    for j in range(len(A)):
        if i != j and A[i] < A[j]:
            count += 1
            break
print(count)

# TC - O(n^2)


"""
Efficient Approach
"""
A = [3, 1, 2]
maximum = A[0]
max_count = 1
for i in range(1, len(A)):
    if maximum < A[i]:
        maximum = A[i]
        max_count = 1
    elif maximum == A[i]:
        max_count += 1
    else:
        continue

print(len(A)-max_count)