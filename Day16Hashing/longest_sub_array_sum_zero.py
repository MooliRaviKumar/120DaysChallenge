A = [1, -2, 1, 2]
#output 3

# 1 -2 -2 2 
# 1 -1 -3 -1
# hm[-1] = 1 --- 4-1 = 3

sum =0
hm = {}
max_sub_array_length = 0
for index, ele in enumerate(A):
    sum += ele
    if sum == 0 and sum not in hm:
        if max_sub_array_length < index:
            max_sub_array_length = index + 1
    if sum in hm:
        if max_sub_array_length < index-hm[sum]:
            max_sub_array_length = index-hm[sum] 
    else:
        hm[sum] = index
print(max_sub_array_length)


