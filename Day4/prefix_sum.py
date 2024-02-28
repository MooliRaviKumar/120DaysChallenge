"""
A = [1, 2 ,3, 4, 5]
Prefix Sum = [1, 3, 6, 10, 15]
sum[1,4] = sum[0,4]- sum[0,0]
sum[1,4] = ps[4] - ps[0]
"""
# prefix sum

A = [1, 2, 3, 4, 5]
ps = []
sum = 0
for i in range(len(A)):
    if len(ps) == 0:
        ps.append(A[i])
    else:
        ps.append(ps[len(ps)-1]+A[i])
print(ps)


    
