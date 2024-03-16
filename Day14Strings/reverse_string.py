def reverse_string(s):
    s1 = ""
    for i in range(len(s)-1, -1, -1):
        s1 += s[i]
    return s1

str = "the sky is blue"
#output blue is sky the
s2 = reverse_string(str)
s3 = ""
start = 0
for i in range(len(s2)):

    if s2[i] == " ":
        s3 += reverse_string(s2[start:i]) + ' '
        start = i+1
    elif i == len(s2)-1:
        s3 += reverse_string(s2[start:i+1])

print(s3)

TC - O(n)
SC - O(n)

