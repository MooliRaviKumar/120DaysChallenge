A = [1, 2, 1, 3, 4, 3]
B = 3
#output 2 3 3 2
hm = {}
arr = []
for index in range(B):
    if A[index] not in hm:
        hm[A[index]] = 1
    else:
        hm[A[index]] += 1
arr.append(len(hm))
print(arr)


for i in range(B, len(A)):
    ele = A[i-B]
    hm[ele] -= 1
    if hm[ele] == 0:
        del hm[ele]
    if A[i] in hm:
        hm[A[i]] += 1
    else:
        hm[A[i]] = 1
    arr.append(len(hm))
print(arr)
