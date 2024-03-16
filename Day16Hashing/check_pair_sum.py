A = 8
B = [3, 5, 1, 2, 1, 2]

#output 1
hm = {}
for ele in B:
    if A-ele in hm:
        print(1)
    else:
        hm[ele] = 1