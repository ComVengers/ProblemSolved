import sys

T = int(input())

for i in range(T):
    _list = list(sys.stdin.readline().strip())
    cnt = 0
    for j in range(len(_list)):
        if _list[j] == '(':
            cnt += 1
        else:
            cnt += -1
        if cnt == -1:
            break # ')'가 더 크면 이미 VPS가 아니므로 break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
    
    
