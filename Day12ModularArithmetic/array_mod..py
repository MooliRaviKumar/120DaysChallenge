A = [1, 4, 3, 4, 9]
# number is 143
# C = 2
# ans is 1 as (143)% 2 = 1

C = 2
k = 0
ans = 0
for i in range(len(A)-1, -1, -1):

    ans = ((ans%C + ((A[i]% C)* pow(10, k)%C)% C))%C
    k = k+1

print(ans)




