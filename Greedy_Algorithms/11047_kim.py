import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
result = 0

for _ in range(N):
    coin.append(int(input()))

coin.reverse()

for i in range(len(coin)):
    if K > 0 and K >= coin[i]:
        result += K // coin[i]
        K = K % coin[i]

print(result)