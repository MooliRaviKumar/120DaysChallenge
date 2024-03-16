str = 'hellO'
# output - 'HELLo'
output = ''
for i in range(len(str)):

    if str[i] >= 'A' and str[i] <= 'Z':
        output += chr(ord(str[i])+32)
    else:
        output += chr(ord(str[i])-32)
print(output)
