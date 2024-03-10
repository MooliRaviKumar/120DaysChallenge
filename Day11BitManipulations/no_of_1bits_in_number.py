A = 11
# 3 as 1011

# lcm of 11 with 2 - 1011


count = 0
while A > 0:
    count += A % 2
    A = A//2
print(count)
