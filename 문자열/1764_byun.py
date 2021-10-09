import sys
n, m = map(int, input().split())

not_hear = set([sys.stdin.readline().strip() for i in range(n)])
not_see = set([sys.stdin.readline().strip() for i in range(m)])

result = sorted(list(not_hear & not_see))
print(len(result))
for name in result:
    print(name)
