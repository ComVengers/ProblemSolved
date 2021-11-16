weight = [] #몸무게
height = [] #키
ranking = [] #덩치 큰 순위
num = 0 #자신보다 덩치가 큰 사람

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)
for i in range(N):
    for j in range(N):
        if i == j: #자기 자신
            continue
        else:
            if (weight[i] < weight[j]) & (height[i] < height[j]): #몸무게도 더 크고 키도 더 큰 경우
                num += 1 #덩치 큰 사람 추가
    ranking.append(num+1)
    num = 0
for i in ranking:
    print(i, end=' ')

