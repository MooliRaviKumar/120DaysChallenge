A = [3, 7, 90, 20, 10, 50, 40]
B = 3

avg = pow(10, 9)-1
sum = 0
for i in range(B):
    sum += A[i]
avg = sum//B
index = 0
for i in range(B, len(A)):
    val = sum - A[i-B] + A[i]
    curr_avg = val//B
    if avg > curr_avg:
        index = i-B+1
        avg = curr_avg



