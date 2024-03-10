"""
110010
1 0 1 0 1
return no consecutive ones
"""

s = "111000"

s = "100001001"

ones = 0
zeros = 0
for i, val in enumerate(s):
    if s[i] == '1':
        ones += 1
    else:
        zeros += 1
print(ones)
print(zeros)
ans = 0
for i, val in enumerate(s):

    if s[i] == '0':
        lc = 0
        for j in range(i-1, -1, -1):
            if s[j] == '1':
                lc += 1
            else:
                break
        rc = 0
        for j in range(i+1, len(s)):
            if s[j] == '1':
                rc += 1
            else:
                break
        if ones > rc+lc:
            ans = max(ans, rc+lc+1)
        else:
            ans = max(ans, rc+lc)
print(ans)


        


