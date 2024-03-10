# after removing index sum of even index = sum of odd index
A = [2, 1, 6, 4]
# after removing index 1
sum = 6 == 6
"""
2 8 
1 5

1 6 4
2 6 4
2 1 4
"""

evensum = []
oddsum = []
for i in range(len(A)):
    if i% 2 == 0 and i == 0:
        evensum.append(A[i])
    elif i %2 == 0:
        evensum.append(evensum[len(evensum)-1] + A[i])
    else:
        evensum.append(evensum[len(evensum)-1])

oddsum = []
for i in range(0, len(A)):
    if i == 0:
        oddsum.append(0)
    elif i==1:
        oddsum.append(A[i])
        print(oddsum)
    elif i!=1 & i%2 != 0:
        oddsum.append(oddsum[len(oddsum)-1] + A[i])
    else:
        print(oddsum)
        oddsum.append(oddsum[len(oddsum)-1])
print(evensum, oddsum)

for i, val in enumerate(A):
    if i == 0:
        if evensum[i+1] == oddsum[i+1]:
            print(True)
    
    else:
        # while removing index
        leftsideevensum = evensum[i-1]
        leftsideoddsum = oddsum[i-1]
        rightsideevensum = evensum[len(evensum)-1] - evensum[i]
        rightsideoddsum = oddsum[len(oddsum)-1] - oddsum[i]
        print("SUM")
        print(leftsideevensum+rightsideoddsum)
        print( leftsideoddsum+rightsideevensum)
        print()
        if leftsideevensum+rightsideoddsum == leftsideoddsum+rightsideevensum:
            print(True, i, "index")
            break

TC = O(n)
SC = O(n)