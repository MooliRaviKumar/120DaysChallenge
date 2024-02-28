"""
Given a number A return is Prime 
"""
A = 6

def get_factors(A):
    i = 1
    count = 0
    while i**i <= A:
        if i **2 == A:
            count += 1
        elif A % i == 0:
            count += 2
        i += 1
    return count

count = get_factors(A)
if count == 2:
    print(True)
else:
    print(False)
