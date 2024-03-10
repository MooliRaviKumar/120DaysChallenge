A =22
B= 3

# 2 * 3 ^0 + 2 * 3^ 1

number = 0
i = 0
while A > 0:
    rem= A % 10 
    number += rem* pow(3, i)
    A = A//10
    i += 1
print(number)
