def fun(n):
    s = 0
    i = 1
    while i*i*i <=n:

        s = s+ i  
        i += 1  
    return s

TC - O(n^(1/3))

1 <= 64 
8 <= 64
27 <= 64
64 <= 64


ans = 0
for i in range(n):
    ans += i*i
return ans

TC - O(n)

def func(n):
    s = 0
    i = 1
    while i < n:
        i = i * 2
        s = s + i
    return s
TC - log(n)
2 4 8 16 -------- n
T(0) = 1
T(n) = 2T(i)+ K

2^k = n
k = log(n)

for(int i=0; i<n, i++){
    for (int j=0; j<=i, j++){
        print(i+j)
    }
}
1 - 1
2 - 2
3 - 3
4 - 4
TC - O(n^2)
