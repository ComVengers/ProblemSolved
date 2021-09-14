N = int(input())
K = int(input())
sensor_list = list(map(int, input().split()))
sensor_list.sort()

result = 0
sum = 0

dist = list()
for i in range(1, N):
    dist.append(sensor_list[i]-sensor_list[i-1])
dist.sort(reverse=True)

for i in range(K):
    result +=dist[i]
print(result)
