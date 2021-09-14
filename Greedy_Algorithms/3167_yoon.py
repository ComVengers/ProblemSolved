def makeList(num): #크기가 num인 list 반환
    a=list()
    for i in range(num):
        a.append('o')
    return a


def freerideMinimum(n, k, getoff, geton):  # 무임승차 최소 -> 같은 사람을 중복으로 검사하는 경우 최소 -> 먼저 탄 사람이 먼저 내림 (선입선출! queue!)
    passengers = list() #현재 탑승한 사람
    sum = 0 #모든 탑승한 사람 수
    check_ok = 0 #검사한 사람 수
    remain = 0 #검사를 했으나 아직 하차하지 않은 사람 수 (검사할 당시, 이미 검사 전적이 있는 사람)
    for i in range(n): # 0 ~ n-1
        if i != 0:
            if remain > getoff[i]:
                remain -= getoff[i]
            else: #remain <= getoff[i]
                remain = 0
            passengers = passengers[getoff[i]: ] # 1. (앞에서부터) 하차시키기
        passengers.extend(makeList(geton[i])) # 2. 승차시키기
        sum += geton[i]
        if i % k == 0: # 만약 i가 k의 배수면, 즉, i가 0, k, 2k, 3k, ...이면 기차표 검사 -> 3. check_ok 업데이트
            check_ok += len(passengers) #현재 탑승한 모든 승객들을 검사
            check_ok -= remain #중복 제거
            remain = len(passengers)
    return sum-check_ok

def freerideMaximum(n, k, getoff, geton):  # 무임승차 최대 -> 같은 사람을 중복으로 검사하는 경우 최대 -> 늦게 탄 사람이 먼저 내림 (후입선출! stack!)
    passengers = list() #현재 탑승한 사람
    sum = 0 #모든 탑승한 사람 수
    check_ok = 0 #검사한 사람 수
    remain = 0 #검사를 했으나 아직 하차하지 않은 사람 수 (검사할 당시, 이미 검사 전적이 있는 사람)
    for i in range(n): # 0 ~ n-1
        if i != 0:
            #이 부분이 특히 다름!
            passengers = passengers[ : len(passengers)-getoff[i] ] # 1. (뒤에서부터) 하차시키기
            if i % k == 1: #만약 검사 직후라면
                remain -= getoff[i]
            else:
                if geton[i-1] <= getoff[i]:
                    remain -= (getoff[i]-geton[i-1])
        passengers.extend(makeList(geton[i])) # 2. 승차시키기
        sum += geton[i]
        if i % k == 0: # 만약 i가 k의 배수면, 즉, i가 0, k, 2k, 3k, ...이면 기차표 검사 -> 3. check_ok 업데이트
            check_ok += len(passengers) #현재 탑승한 모든 승객들을 검사
            check_ok -= remain #중복 제거
            remain = len(passengers)
    return sum-check_ok

# 역은 총 N개이고, K개의 역을 지날 때마다 표 검사
N, K = map(int, input().split(' '))

getoff = list()
geton = list()

# 각 역에서 하차한 사람 수, 승차한 사람 수를 각 리스트에 저장
for i in range(N):
    off, on = map(int, input().split(' '))
    getoff.append(off)
    geton.append(on)

min=freerideMinimum(N, K, getoff, geton)
max=freerideMaximum(N, K, getoff, geton)

print('{0} {1}'.format(min, max))

