import sys
n = int(input())

size_list = []
for i in range(n):
    size_list.append(list(map(int,sys.stdin.readline().split())))

for i in size_list:
    rank = 1
    for j in size_list :
        if(i[0]<j[0])&(i[1]<j[1]):
            rank +=1
    print(rank)
