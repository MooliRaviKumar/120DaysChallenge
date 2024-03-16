A = ['S', 'c', 'A', 'B', 'D', 'E', 'f']

for i in range(len(A)):
    if A[i] >= 'A' and A[i]<= 'Z':
        A[i] = chr(ord(A[i])+32)

# 'F' --- 95 
print(A)

# TC = O(n)
# Sc = O(1)