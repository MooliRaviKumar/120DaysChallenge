# A, B, C
# claculate the value of (A^B)%C

# 2, 3, 3  --------------(2^3)%3

A = 2
B = 3
C = 3

ans = ((A%C)^(B%C)%C)
print(ans)