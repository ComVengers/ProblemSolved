import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
K = int(input())
sensor = map(int, input().split())
sensor = list(sensor)

sensor.sort()

dist = []
for i in range(N-1):
    dist.append(sensor[i+1]-sensor[i])

dist.sort()
dist.reverse()
if K>1:
    del dist[:K-1]

sum_list = sum(dist)
print(sum_list)
