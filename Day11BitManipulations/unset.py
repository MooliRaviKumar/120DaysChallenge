A= 4
B = 1
# ans - 4
# if bith set make it to usnset

if A | (1 << B)== A:
    A =  A ^ (1 << B)
    print(A)
else:
    print(A)
# 4 
# 100
# 010
# 110    
# 100    
# 110
# 010
# 100        
# 100
    