A = [10, 1, 3, 4, 3, 5, 6]
# output - 5

# hm = {}
# for i, ele in enumerate(A):
#     if ele in hm:
#         count = hm[ele][0]
#         count += 1
#         hm[ele] = [count, hm[ele][1]]
#     else:
#         count = 1
#         hm[ele] = [count, i]
# print(hm)
# min_index = len(hm)
# ans =-1
# for ele in hm:
#     if hm[ele][0] > 1 and min_index > hm[ele][1]:
#         min_index = hm[ele][1]
#         ans = ele
# print(ans)

hm = {}
min = len(A)
for i in range(len(A)-1, -1, -1):
    if A[i] in hm:
        min = i
    else:
        hm[A[i]] = 1
if min != -1:
    print(A[min])
else:
    print(-1)
