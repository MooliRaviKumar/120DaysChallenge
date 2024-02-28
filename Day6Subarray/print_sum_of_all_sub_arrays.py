A = [4, 5, 2]
# 4
# 4 5
# 4 5 2
# 5 
# 5 2
# 2
l = 0
sum = 0
ps = []
i = 0
while i  < len(A):
    if i == 0:
        ps.append(A[i])
    else:
        ps.append(ps[len(ps)-1] + A[i])
    i += 1

print(ps)
l = 0
sum = 0
while l < len(A):

    r = l
    while r < len(A):
        if l == 0:
            sum += ps[r]
        else:
            sum += ps[r]-ps[l-1]
        # k = l
        # while k <=r:
        #     sum = sum + A[k]
        #     k += 1
        r += 1
    l += 1
print(sum)

"""
4 5 9
5 7
2

"""