a = int(input())

for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for j in s:
        if j =='(':
            sum += 1
        elif j ==')':
            sum -= 1
        # 닫는 괄호 보다 여는 괄호가 더 많이 나왔을 때
        if sum == -1:
            print('NO')
            break

    if sum == 0:
        print('YES')
    elif sum > 0:
        print('NO')
