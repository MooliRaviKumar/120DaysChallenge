# 11111
#   0 
# 11111
# A & (1 << B) == 0  if B is unset else B is set
# A | (1 << B) == A if B is set 
# A ^ (1 << B)  bit B will be swapped
A = 4
B = 2

# 100
#  1
# 000

if A & (1 << B) == 0:
    print (f"bit {B}, is unset")
else :
   print(f"bit {B} is set")
