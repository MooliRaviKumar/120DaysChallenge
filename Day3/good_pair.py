A = [1,2,3,4]
B = 7
3 + 4
# i != j and A[i] + A[j] == B
hs = set()
for i in range(len(A)):
    hs.add(A[i])

count = 0
for i in range(len(A)):
    if B-A[i] in hs:
        count += 1
        hs.remove(A[i])
print(count)

hm = {}
for i in range(len(A)):
    if A[i] not in hm:
        hm[A[i]] = 1
    else:
        hm[A[i]] += 1

A = [1,2,3,4]
count = 0
for i in range(len(A)):
    if B-A[i] in hm:
        count += hm[A[i]] * hm[B-A[i]]
        del hm[A[i]]
        del hm[B-A[i]]
    elif B-A[i] == A[i]:
        count -= 1
print(count)
    