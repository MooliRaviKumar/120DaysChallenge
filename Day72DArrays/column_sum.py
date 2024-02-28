"""You are given a 2D integer matrix A, return 
a 1D integer array containing column-wise sums of original matrix.
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

{15,10,13,16}

"""
A = [[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]
ans = []
for j in range(len(A[0])):
    sum = 0
    for i in range(len(A)):
        sum += A[i][j]
    ans.append(sum)
print(ans)
