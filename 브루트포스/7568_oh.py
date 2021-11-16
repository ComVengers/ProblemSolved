import sys
N = int(input())
weight = []
height = []

for i in range(N):
    n, m = map(int, input().split())
    weight.append(n)
    height.append(m)

for i in range(N):
    rank = 1
    for j in range(N):
        if weight[i]<weight[j] and height[i]<height[j]:
            rank += 1
    print(rank, end = ' ')
