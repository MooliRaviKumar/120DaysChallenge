A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]

# ps = []
# sum = 0
# for i in range(len(A)):
#     if len(ps) == 0:
#         ps.append(A[i])
#     else:
#         ps.append(ps[len(ps)-1]+A[i])
# print(ps)

sum_arr = []
for k in range(len(B)):
    l = B[k][0]
    r = B[k][1]
    s = ps[r]- ps[l-1] if k > 0 else ps[r]
    sum_arr.append(s)
print(sum_arr)
"""
sum[2, 3] = sum[0,3] - sum [0, 1]
          = ps[r] - ps[l-1]
"""

