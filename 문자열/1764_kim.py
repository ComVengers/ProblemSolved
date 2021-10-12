import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_listen_people = set()
not_see_people = set()
count = 0
answer = []

for _ in range(N):
    L = input()
    not_listen_people.add(L.rstrip('\n'))

for _ in range(M):
    S = input()
    not_see_people.add(S.rstrip('\n'))

names = list(not_listen_people & not_see_people)           #intersection
names.sort(key=lambda x:x)

print(len(names))

for name in names:
    print(name)