"""
i,j i<j and s[i]='a' s[j]= 'g'
"""
s = "baagdcag"
total_count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == 'a' and s[j] == 'g':
            total_count += 1
print(total_count)


"""
TC - O(n^2)
SC - O(1)
"""


s = "baagdcag"
a_count = 0
g_count = 0

for k in range(len(s)-1, -1, -1):
    if s[k] == 'a':
        a_count += g_count
    elif s[k] == 'g':
        g_count += 1
    else:
        continue
print(a_count)

TC - O(size of s)


