A = [5, 7, 100, 11]
B = 20

count = 0
for i in range(len(A)):
    if A[i] <= B:
        count += 1

min_swaps = len(A) 
ans = len(A)
greater = 0
for i in range(count):
    if A[i] > B:
        greater += 1
ans = min(ans, greater)

for i in range(count, len(A)):
    if A[i-count] > B:
        if A[i] > B:
            greater += 1
        else:
            greater -= 1
    else:
        if A[i] > B:
            greater += 1
    
    ans = min(ans, greater)
print(ans)