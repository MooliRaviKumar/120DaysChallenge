A = [-7, 1, 5, 2, -4, 3, 0]
ps = []
sum = 0
for i in range(len(A)):
    if len(ps) == 0:
        ps.append(A[i])
    else:
        ps.append(ps[len(ps)-1]+A[i])
print(ps)
ss = []
k = 0
for j in range(len(A)-1, -1, -1):
    
    if len(ss) == 0:
        ss.append(A[j])
    else:
        ss.append(ss[len(ss)-1] + A[j])

print(ss)

for i in range(len(A)):
    if ps[i] == ss[len(ss)-1-i]:
        print(i)

A = [-7, 1, 5, 2, -4, 3, 0]
ps = [-7, -6, -1, 1, -3, 0, 0]
ss = [0, 3, -1, 1, 6, 7, 0]