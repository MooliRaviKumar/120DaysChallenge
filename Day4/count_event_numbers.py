A = [1, 2, 3, 4, 5]

ps = []
for i in range(len(A)):
    if A[i]%2 == 0:
        if len(ps) == 0:
            ps.append(1)
        else:
            ps.append(ps[len(ps)-1]+1)
    else:
        if i == 0:
            ps.append(0)
        else:
            ps.append(ps[len(ps)-1])

ss = []
k = 0
for j in range(len(A)-1, -1, -1):
    
    if A[j]%2 == 0:
        if len(ss) == 0 :
            ss.append(1)
        else:
            ss.append(ss[len(ss)-1] + 1)
    else:
        if j == len(A)-1:
            ss.append(0)
        else:
            ss.append(ss[len(ss)-1])

A = [1, 2, 3, 4, 5]
B = [ [0, 2],
      [2, 4],
      [1, 4] ]
ans = []
length = len(B)

for i in range(length):
    l = B[i][0]
    r = B[i][1]
    if l == 0:
        count = ps[r]
    else:
        count = ps[r]-ps[l-1]
    ans.append(count)

print(ans)        