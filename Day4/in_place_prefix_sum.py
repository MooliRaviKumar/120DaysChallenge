A = [1, 2, 3, 4, 5]

sum = 0
for i in range(len(A)):
    if i != 0:
        sum = sum + A[i]
        A[i] = sum
    else:
        sum = A[i]
        
print(A)
A = [1, 2, 3, 4, 5]
for i in range(1,len(A)):
    A[i] += A[i-1]

print(A)