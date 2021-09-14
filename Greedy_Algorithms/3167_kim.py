import sys
input = sys.stdin.readline

def minPassenger():
    check = 0
    not_check = 0
    idx = 1
    result = 0
    for i in range(1, N+1):
        if i == 1:
            check += passenger[0][1]
        elif i == idx+3:
            if check == 0:
                not_check -= passenger[i-1][0]
            else:
                check -= passenger[i-1][0]
            check += not_check
            not_check = 0
            idx += 2
        else:
            check -= passenger[i-1][0]
            if check < 0:
                not_check -= abs(check)
                result += abs(check)
                check = 0
            not_check += passenger[i-1][1]
    return result

def maxPassenger():
    check = 0
    not_check = 0
    idx = 1
    result = 0
    for i in range(1, N+1):
        if i == 1:
            check += passenger[0][1]
        elif i == idx+3:
            if not_check == 0:
                check -= passenger[i-1][0]
            else:
                not_check -= passenger[i-1][0]
            check += not_check
            not_check = 0
            idx += 2
            not_check += passenger[i-1][1]
        else:
            if not_check == 0:
                check -= passenger[i-1][0]
            else:
                not_check -= passenger[i-1][0]
                if not_check < 0:
                    check -= abs(not_check)
                    result += (passenger[i-1][0]-abs(not_check))
                    not_check = 0
                else:
                    result += passenger[i-1][0]
            not_check += passenger[i-1][1]
    return result

N, K = map(int, input().split())
passenger = []

for _ in range(N):
    outIn = tuple(map(int, input().split()))
    passenger.append(outIn)

print(minPassenger(), maxPassenger())

