import sys
input = sys.stdin.readline

stick = list(input().rstrip('\n'))
stack = []
total = 0

for i in range(len(stick)):

    if stick[i] == ')':
        stack.pop()

        if stick[i-1] == '(':       # 레이저라면
            total += len(stack)
        else:                       # 막대의 끝이라면
            total += 1
    else:
        stack.append(stick[i])

print(total)