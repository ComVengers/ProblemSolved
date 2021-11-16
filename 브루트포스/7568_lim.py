n = int(input())
dungchi = []

for i in range(n):
    w, h = map(int, input().split())
    dungchi.append((w,h))

for i in dungchi:
    rank = 1
    for j in dungchi:              # 비교 대상
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank)