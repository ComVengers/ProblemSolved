import sys

N, M = map(int, input().split())
d_list = set()
b_list = set()
for i in range(N):
    name = sys.stdin.readline().strip()
    d_list.add(name)

for i in range(M):
    name = sys.stdin.readline().strip()
    b_list.add(name)


db_list = sorted(d_list & b_list)

print(len(db_list))
for i in range(len(db_list)):
    print(db_list[i])
        
        
