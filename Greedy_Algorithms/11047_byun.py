N, K = map(int, input().split())
coin_list = list()
for i in range(N):
    coin_list.append(int(input()))
result = 0

for i in reversed(range(N)):
    result += int(K/coin_list[i])
    K = int(K%coin_list[i])

print(result)
