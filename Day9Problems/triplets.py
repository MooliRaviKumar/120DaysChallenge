A = [1, 2, 3]

2
# 1,2,3   1,2,4
ans = 0
for i in range(len(A)):
    l = 0
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            l += 1
    if l == 0:
        continue
    r = 0
    for j in range(i+1, len(A)):
        if A[i] < A[j]:
            r += 1
    ans = max(ans, l*r)
print(ans)

