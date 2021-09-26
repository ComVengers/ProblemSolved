n, k = map(int, input().split())
coin = []
cnt = 0
for i in range(n):
    c = int(input())
    coin.append(c)
coin.reverse()
for i in range(n):
    if k == 0:
        break
    else:
        if k >= coin[i]:
            cnt += k // coin[i]
            k %= coin[i]
print(cnt)
