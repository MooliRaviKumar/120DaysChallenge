"""
Given a array A of length N, Also given are integers B and C 
Return 1 if there exists a subarray with length B having C and 0 otherwise
"""
A = [4, 3, 2, 6, 1]
B = 3
C = 11
"""4 7  9 15 16"""
ps = []
for i in range(len(A)):
    if i == 0 :
        ps.append(A[i])
    else:
        ps.append(ps[len(ps)-1]+A[i])
hs = set()
for i in range(len(A)-3):
    print(A[i])
    j = i+B-1
    if i == 0:
        if ps[j] == C:
            print(True)
    else:
        val = ps[j]-ps[i-1]
        if val == C:
            print(True)


# TC - O(n)
# Sc - O(n)
print(f"sliding window approach")
sum = 0
for i in range(B):
    sum += A[i]
print(f"sum : {sum}")    
if sum == C:
    print(True)
for i in range(B, len(A)):
    val = sum + A[i] - A[i-B]
    if val == C:
        print(True)
