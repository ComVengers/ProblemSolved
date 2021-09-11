import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
distance = list(map(int, input().split()))

# 집중국의 개수가 센서의 개수보다 많으면 센서의 개수만큼 설치하면 됨
if K >= N:
    print(0)
else:
    distance.sort()
    diff = []

    # 정렬된 집중국의 거리 차이를 구한다
    for i in range(len(distance)-1):
        diff.append(distance[i+1]-distance[i])

    # 거리 차이를 역순으로 정렬
    diff.sort(reverse=True)

    # 거리 차이가 가장 큰 숫자를 0으로 바꾼 후 합을 구한다
    for i in range(K-1):
        diff[i] = 0
    print(sum(diff))