A = [1, 2, 3, 4, 5]

L = 0
while L < len(A):
    R= L
    while R<len(A):
        k = L
        while k<=R:
            print(A[k], end = "")
            k  += 1
        print()
        R += 1
    print()
    L += 1

# TC - O(n^3)
# SC - O(1)
