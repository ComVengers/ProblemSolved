import sys
n = int(input())
friend = []
f_friend = []
a_list=[]
b_list=[]

for i in range(n):
    friend.append(0)

m = int(input())
for i in range(m):
    a,b = map(int, input().split())
    if a == 1:
        a_list.append(b)
    else:
        b_list.append([a,b])

for i in range(len(a_list)):
    friend[a_list[i]-1] = 1

for i in range(len(b_list)):
    for j in range(len(a_list)):
        if b_list[i][0] == a_list[j]:
            friend[b_list[i][1]-1] = 1
            

print(friend.count(1))
