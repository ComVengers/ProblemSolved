import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
distance = list(map(int, input().split()))

# 집중국의 개수가 센서의 개수보다 많으면 센서의 개수대로 집중국을 세우면 됨!
if K >= N:
    print(0)
else:
    distance.sort()
    diff = []

    # 집중국 사이의 거리차를 계산
    for i in range(len(distance)-1):
        diff.append(distance[i+1]-distance[i])

    # 거리차가 큰 순으로 정렬
    diff.sort(reverse=True)

    # (집중국의 개수 - 1)개 만큼 거리차순이 큰거부터 0으로 바꿔준 후 합
    for i in range(K-1):
        diff[i] = 0
    print(sum(diff))
