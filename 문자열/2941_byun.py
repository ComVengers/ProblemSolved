import sys
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n_list = input()
result = []

i = 0

while i<len(n_list):
    str = n_list[i:i+2]

    if(str=='dz'):
        str = n_list[i:i+3]
        result.append(str)
        i+=3
        continue

    if str in alphabet :
        result.append(str)
        i+=1

    else:
        result.append(n_list[i])
    i+=1

print(len(result))
