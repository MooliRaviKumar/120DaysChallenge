"""
Product of a array and divide by its element
"""
A = [5, 1, 10, 1]
ps = []
for i in range(len(A)):
    if i == 0:
        ps.append(A[i])
    else:
        ps.append(ps[len(ps)-1] * A[i])

ss = []
for j in range(len(A)-1, -1, -1):
    if j == len(A)-1:
        ss.append(A[j])
    else:
        ss.append(ss[len(ss)-1] * A[j])
print(ss)

arr = []
for k in range(len(A)):
    if k == 0:
        arr.append(ss[len(ss)-k-2])
    elif k == len(A)-1:
        arr.append(ps[len(ps)-2])
    else:
        arr.append(ps[k-1] * ss[len(ss)-k-2])
print(arr)



