# 세로길이 2 => min(4,(가로길이 + 1) //2)
# 세로길이 3 => min(4, 가로길이)
# 세로길이 4 이상 => 5+(가로길이-7)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = 0

if N == 1:
    result = 1
elif N == 2:
    result = min(4,(M+1)//2)
elif M < 7:
    result = min(4, M)
else:
    result = 5+M-7

print(result)
