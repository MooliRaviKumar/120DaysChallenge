A = 5
B = 12
C = [2, 1, 3, 4, 5]

ans = 0
for l in range(A):
    sum = 0
    for r in range(l, A):
        sum += C[r]
        if sum <= B:
            ans = max(sum, ans)
print(ans)

