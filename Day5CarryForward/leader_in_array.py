"""
 Leader in a array - strictly greater than elements its right side 
"""

A = [16, 17, 4, 3, 5, 2]

ans = []
leader = -1
for i in range(len(A)-1, -1 , -1):
    if i == len(A)-1:
        ans.append(A[i])
        leader = A[i]
    elif  A[i] > leader:
        ans.append(A[i])
        leader = A[i]
print(ans)