A = 'aaaabaaa'

# output - aaabaa
# for i in range(len(A)):
#     for j in range(i, len(A)):
        # sub arrays - i<=s<=j
        # for every sub array find palindrome and start and end if it is greater than remaining 
        # the palindromes just return it

def palindrome_string(i, arr):

    s = i-1
    e = i+1
    while s > -1 and e < len(arr):
        if arr[s] != arr[e]:
            return s+1,e
        s-= 1
        e += 1
    return s+1, e

palindrome = ''
start = 0
max = 0
ans = []
for i in range(0, len(A)-1):
    start, end = palindrome_string(i, A)
    print(start, end)
    if end-start+1 > max:
        ans = A[start:end]
        max = end-start+1

print(ans)
print(max)
