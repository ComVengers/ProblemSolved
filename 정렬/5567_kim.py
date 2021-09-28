import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = []
b = []
invite = []
result = 0

for _ in range(m):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)

for i in range(m):
    if a[i] == 1 and b[i] not in invite:
        invite.append(b[i])

for j in range(len(invite)):
    for k in range(m):
        if invite[j] == a[k] and b[k] not in invite:
            result += 1

result += len(invite)
print(result)
