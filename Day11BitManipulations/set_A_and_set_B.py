A = 4
B = 4
A = 3
B = 5
# 3th bit set means -  1000  1<<3
# 5th bit set means -100000 1 <<5
# total means 1<<3 + 1<<5 = (2pow3 + 2pow5)

if A==B:
    print(pow(2, B))
else:
    print(pow(2, A)+ pow(2, B))
