A = [4, -1, 1, 2, -2, 3 , -3]
# output 1

# Brute Force Approach

# for i in range(len(A)):
#     for j in range(i, len(A)):

#         start = i
#         end = j 
#         sum_zero = 0
#         while start <= end:
#             sum_zero += A[start]
#             start += 1
#         if sum_zero == 0:
#             print(True)
#             break
# TC - O(n^3)
# SC - O(1)
# ps = []
# for i in range(len(A)):
#     if i == 0:
#         ps.append(A[i])
#     else:
#         ps.append(ps[i-1]+A[i])
# print(ps)

# for i in range(len(A)):
#     for j in range(i, len(A)):
#         if i == 0:
#             if ps[j] == 0:
#                 print(True)
#         else:
#             print(i, j)
#             if ps[j] - ps[i-1] == 0:
#                 print(True)
# TC - O(n^2)
# SC - O(n)


hm = {}
sum = 0
# for i in range(len(A)):
#     sum += A[i]
#     if sum == 0:
#         print(1)
#         break
    
#     if sum in hm:
#         print(1)
#         break
#     else:
#         hm[sum] = 1

for ele in A:
    sum += ele
    if sum == 0:
        print("sum zero exist")
    if sum in hm:
        print("sum zero exist")
    else:
        hm[sum] = 1
