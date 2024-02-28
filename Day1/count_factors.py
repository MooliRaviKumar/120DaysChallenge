"""
Given a number A find the count of its factors
"""
number = 5

"""
Factor : divisible any number that number is become a factor
"""
count = 0
for i in range (1,number+1):
    if number % i == 0:
        count += 1
print(count)

"""if i is a factor then N/i also a factor"""
"""
i * N/i = number
"""
i = 1
count = 0
number = 5
while i*i <= number:
    if i**2 == number:
        count += 1
    elif  number % i == 0:
        count += 2
    i += 1
print(count)