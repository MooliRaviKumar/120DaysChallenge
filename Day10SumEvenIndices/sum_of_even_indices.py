A = [1, 2, 3, 4, 5]
B = [[0,2], [1, 4]]

ps = []
for i in range(len(A)):
    if i == 0:
        ps.append(A[i])
    elif i % 2== 0:
        ps.append(ps[len(ps)-1]+A[i]) 
    else:
        ps.append(ps[len(ps)-1])

print(ps)
ans = []
for i in range(0,len(B)):
    l = B[i][0]
    r = B[i][1]
    ans.append(ps[r]-ps[l-1] if l > 0 else ps[r])
print(ans)
    
    
