import sys
a_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
text = input()

for i in a_list:
    text = text.replace(i,'o')
print(len(text))
