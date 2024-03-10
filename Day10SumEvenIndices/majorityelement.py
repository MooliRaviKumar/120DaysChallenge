A = [2, 1, 2]

# Majority is like if element appears more than n/2

hm = {}
for ele in A:
    if ele not in hm:
        hm[ele] = 1
    else:
        hm[ele] += 1

print (hm)

length = len(A)

majority_element = pow(10,-9)-1
for key, value in hm.items():
    if value > (length//2):
        majority_element = value
print(majority_element)





arr = [3, 4, 3, 2, 4, 4, 4, 4]

# maj_index = 0, count = 1

# 3!=4
# count -1 = 1-1 = 0
# count == 0

maj_ele = -1

count = 0

for ele in arr:

    if count == 0:
        maj_ele = ele
        count += 1
    elif ele != maj_ele:
        count -= 1
    else:
        count += 1
print(maj_ele, count)

total_count = 0
if count != 0:
    for ele in arr:
        if ele == maj_ele:
            total_count += 1
print(total_count)

if total_count > (length//2):
    print(maj_ele , "is  a majority element")

