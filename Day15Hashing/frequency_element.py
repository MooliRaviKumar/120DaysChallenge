arr = [1, 2, 1, 1]

hm = {}
for ele in arr:
    if ele in hm:
        hm[ele] += 1
    else:
        hm[ele] = 1
ans = []
for ele in arr:
    if ele in hm:
        ans.append(hm[ele])
        del hm[ele]
print(ans)