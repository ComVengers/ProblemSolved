N = int(input())
people = []
ranking = []

for _ in range(N):
    dungchi = tuple(map(int, input().split()))
    people.append(dungchi)

for i in range(N):
    rank = 0
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranking.append(rank)

for r in range(N):
    print(ranking[r]+1)



