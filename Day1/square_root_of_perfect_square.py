"""
Square root of Perfect square otherwise -1
"""
A = 25

i = 1
count = 0
ans = False
while i <= pow(A,1/2):
    if i * i == A:
        ans = True
        # print (i)
    i += 1
# print(ans)

"""
binary search
"""
A = 26
right = 26
left = 1

while left <= right:

    mid = (left+right)//2
    if mid*mid == A:
        print(mid)
        break
    elif mid*mid < A:
        left = mid + 1
    else:
        right = mid -1

TC - O(log(A))
