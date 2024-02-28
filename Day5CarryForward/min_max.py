# Closest Min Max of a Array 
"""
A = [1, 3, 2]
count = 2
"""

ans = 0
A = [1, 3, 2]
A = [3, 7, 2, 4, 1, 6]
minimum = min(A)
maximum = max(A)
ans1 = len(A)
ans2 = len(A)

for i, value in enumerate(A):
    if A[i] == minimum:
        for j in range(i+1, len(A)):
            if A[j] == maximum:
                ans1 = j-i+1
    elif A[i] == maximum:
        for j in range(i+1, len(A)):
            if A[j] == minimum:
                ans2 = j-i+1
    ans = min(ans1, ans2)
# print(ans)

ans1 = len(A)
index1 = -1
for i, value in enumerate(A):
    if A[i] == minimum:
        index1 = i
        print(minimum, index1)
    elif A[i] == maximum:
        ans1 = min(ans1, i-index1+1)
        print(f"ans1:{ans1}")
ans2 = len(A)
index2 = -1
i = 0
print(f"ans1: {ans1}")
for i, value in enumerate(A):
    if A[i] == maximum:
        index2 = i
        print(maximum, index2)
    elif A[i] == minimum:
        ans2 = min(ans2, i-index2+1)
        print(f"ans2: {ans2}")
ans = min(ans1, ans2)
print(ans)
min_index = -1
max_index = -1
ans = len(A)
A = [3, 1, 2, 4, 7, 6]
minimum = 1
maximum = 7
i = 0
while i< len(A):
    if A[i] == minimum:
        if max_index != -1:
            ans = min(ans, i-max_index+1)
        min_index = i
        print(f"min_index : {min_index}")

    elif A[i] == maximum:
        if min_index != -1:
            ans = min(ans, i-min_index+1)
        max_index = i
    i += 1
print(f"ans: {ans}")
print(min_index, max_index)            
        


1,2,5,1,4,2,3,5

