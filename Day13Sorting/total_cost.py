A = [2, 3, 4]

# 2 - 9
# 3 - 16
# 4 - 20

# 4 - 9
# 3 - 14
# 2 - 16

A.sort()
sum = 0
length = len(A)
for ele in A:
    sum += length*ele
    length -= 1

print(sum)
