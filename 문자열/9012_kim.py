import sys
input = sys.stdin.readline

n = int(input())
strings = list()
bracket = list()

for _ in range(n):
    strings.append(input().rstrip())

for i in range(n):
    temp = True
    bracket.clear()
    for j in range(0, len(strings[i])):
       if strings[i][j] == "(":
           bracket.append(strings[i][j])
       else:
           if len(bracket) != 0:
               bracket.pop()
           else:
               temp = False

    if len(bracket) != 0:           # 괄호가 stack에 남아 있다면
        temp = False                # 실패로 간주하기 위해 False로 설정

    if temp:
        print("YES")
    else:
        print("NO")